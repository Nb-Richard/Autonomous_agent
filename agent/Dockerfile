FROM python:3.12-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN python -c "from sentence_transformers import SentenceTransformer; \
 SentenceTransformer('all-MiniLM-L6-v2')"

COPY rag/ ./rag/
COPY mcp_server/ ./mcp_server/
COPY agent/ ./agent/
COPY docs/ ./docs/

CMD ["python", "-m", "agent.agent"]