# DeepSeek in Docker

This project runs DeepSeek locally with Docker Compose by combining:

- an Ollama inference service
- a lightweight web UI served by Nginx

## Overview

- Ollama API endpoint: `http://localhost:11434`
- Web UI endpoint: `http://localhost:3001`
- Model data persisted under `ollama-models/`

## Project Files

- `docker-compose.yml`
- `README.md`
- `web/index.html`
- `web/ollama.js`
- `web/style.css`
- `web/showdown.min.js`
- `ollama-models/`

## Requirements

- Docker Desktop (or Docker Engine + Docker Compose)
- Enough RAM and disk for the selected model

## Quick Start

1. Start Ollama:

```bash
docker compose up -d ollama
```

2. Verify Ollama is running:

- Open `http://localhost:11434`
- Expected message: `Ollama is running`

3. Pull DeepSeek model:

```bash
docker compose exec ollama ollama pull deepseek-r1:7b
```

4. Start web service:

```bash
docker compose up -d web
```

5. Open the UI:

- `http://localhost:3001`

## Daily Usage

Start all services:

```bash
docker compose up -d
```

Stop all services:

```bash
docker compose down
```

View logs:

```bash
docker compose logs -f
```

## Compose Configuration

```yaml
services:
  ollama:
    image: ollama/ollama
    volumes:
      - ./ollama-models:/root/.ollama
    ports:
      - 11434:11434

  web:
    image: nginx:1.27.3-alpine
    volumes:
      - ./web:/usr/share/nginx/html
    ports:
      - "3001:80"
```

## Troubleshooting

- Blank page on `localhost:3001`:

```bash
docker compose restart web
```

- Model errors or no response:

```bash
docker compose logs -f ollama
```

- Model missing after restart: verify `./ollama-models:/root/.ollama` exists in compose and `ollama-models/` contains model data.
