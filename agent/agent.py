import asyncio, os
import ollama
from pathlib import Path
from contextlib import AsyncExitStack
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from rag.retriever import retrieve_context

MODEL = 'llama3.2'  # llama3.1 is more reliable than llama3.2 for tool-calling
MCP_SERVER = StdioServerParameters(
 command='python',
 args=['-m', 'mcp_server.server'],
)

PROMPT_PATH = Path(__file__).parent / 'prompts' / 'system.md'
SYSTEM_PROMPT = PROMPT_PATH.read_text(encoding='utf-8')

ollama_client = ollama.Client(host=os.getenv('OLLAMA_HOST', 'http://localhost:11434'))


def mcp_tools_to_ollama(mcp_tools) -> list:
 return [
  {
   'type': 'function',
   'function': {
    'name': t.name,
    'description': t.description,
    'parameters': t.inputSchema,
   }
  }
  for t in mcp_tools
 ]


async def run_agent(user_query: str) -> str:
 async with AsyncExitStack() as stack:

  stdio_transport = await stack.enter_async_context(
   stdio_client(MCP_SERVER)
  )
  read, write = stdio_transport
  session = await stack.enter_async_context(
   ClientSession(read, write)
  )
  await session.initialize()

  tools_response = await session.list_tools()
  tools = mcp_tools_to_ollama(tools_response.tools)
  print(
   f'[MCP] {len(tools)} outils disponibles : '
   f"{[t['function']['name'] for t in tools]}"
  )

  context = retrieve_context(user_query)
  messages = [
   {'role': 'system', 'content': SYSTEM_PROMPT},
   {
    'role': 'user',
    'content': f'Context:\n{context}\n\nQuestion: {user_query}'
   },
  ]

  for _ in range(5):
   response = ollama_client.chat(
    model=MODEL,
    messages=messages,
    tools=tools
   )
   msg = response.message

   if not msg.tool_calls:
    return msg.content

   messages.append({
    'role': 'assistant',
    'content': '',
    'tool_calls': [
     {
      'function': {
       'name': tc.function.name,
       'arguments': dict(tc.function.arguments)
      }
     }
     for tc in msg.tool_calls
    ]
   })

   for tc in msg.tool_calls:
    print(
     f'[MCP] Tool call: '
     f'{tc.function.name}({dict(tc.function.arguments)})'
    )

    tool_result = await session.call_tool(
     tc.function.name,
     arguments=dict(tc.function.arguments),
    )

    content = (
     tool_result.content[0].text
     if tool_result.content
     else '{}'
    )

    messages.append({
     'role': 'tool',
     'content': content
    })

  return 'Sorry, I was unable to process this request.'


async def main():
 print("AI agent ready. Type 'quit' to exit.\n")

 while True:
  query = input('You : ').strip()

  if query.lower() == 'quit':
   break

  answer = await run_agent(query)
  print(f'Agent: {answer}\n')


if __name__ == '__main__':
 asyncio.run(main())