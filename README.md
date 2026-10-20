# Agentic AI Assistant for ERP Inventory & Order Management


## Overview

This project explores an **agentic AI assistant** for a simulated enterprise resource planning (ERP) environment. Instead of relying on a language model's general knowledge alone, the assistant combines two complementary sources of information:

- **Live business data** - products, stock quantities, and customer orders retrieved from an Express.js API through MCP tools.
- **Business knowledge** - product specifications, stock policies, delivery information, warranties, and internal procedures retrieved through a ChromaDB-based RAG pipeline.

A locally hosted LLM (**llama3.1**) running with **Ollama** decides when to use a tool, interprets the retrieved information, and formulates a natural-language response. The components can be run locally or orchestrated with **Docker Compose**.

## Key Features

- **Local LLM inference:** Run a tool-capable model such as `llama3.1` using Ollama.
- **Tool discovery and execution:** Discover business tools through the official MCP Python SDK and call them as needed.
- **Retrieval-augmented answers:** Retrieve relevant document passages with Sentence Transformers and ChromaDB.
- **ERP-style REST API:** Access product details, current inventory, and orders through an Express.js service.
- **ReAct-inspired agent loop:** Let the model alternate between deciding on actions, calling tools, and synthesizing answers.
- **Versioned system instructions:** Keep the agent's behavioral instructions in `agent/prompts/system.md`.
- **Container orchestration:** Run the API, Ollama, ChromaDB, and agent services with Docker Compose.

## Tech Stack

| Layer | Technologies | Purpose |
| --- | --- | --- |
| LLM and orchestration | Python, Ollama, Llama 3.1 | Understand questions, decide on tools, generate responses |
| Tool integration | MCP Python SDK (`FastMCP`, `ClientSession`), HTTPX | Expose and invoke business API operations |
| RAG | ChromaDB, Sentence Transformers | Embed, store, and retrieve business documents |
| Embeddings | `all-MiniLM-L6-v2` | Convert document passages and queries into vectors |
| Business backend | Node.js, Express.js, CORS | Serve products, stock, orders, and health endpoints |
| Deployment | Docker, Docker Compose | Package and connect services |
