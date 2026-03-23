# Graphdb-Deepseek

This repository contains practical experiments for running DeepSeek locally and learning graph database workflows.

## Projects

### 1. DeepSeek in Docker
Directory: `deepseek_in_docker/`

- Runs DeepSeek through Ollama in Docker
- Hosts a simple web UI via Nginx
- Includes a dedicated setup guide

Entry points:
- `deepseek_in_docker/README.md`
- `deepseek_in_docker/docker-compose.yml`

### 2. DeepSeek on macOS (Apple Silicon)
Directory: `deepseek_in_mac/`

- Local inference and RAG examples on macOS
- Python app and notebook workflow

Entry points:
- `deepseek_in_mac/README.md`
- `deepseek_in_mac/requirements.txt`
- `deepseek_in_mac/app.py`

### 3. GraphDB in Docker (Memgraph)
Directory: `graphdb_in_docker/`

- Graph database learning materials with Memgraph
- Notebook-based exercises using Cypher and GQLAlchemy

Entry points:
- `graphdb_in_docker/README.md`
- `graphdb_in_docker/notebook/`

## Repository Hygiene

- Root ignore rules are centralized in `.gitignore`
- Local model/cache artifacts are excluded from source control
- Temporary OS/editor files are ignored

## Quick Start

If you want to start with local DeepSeek in Docker:

1. Go to `deepseek_in_docker/`
2. Follow `deepseek_in_docker/README.md`
