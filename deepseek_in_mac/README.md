# DeepSeek Local Inference on macOS

This project runs DeepSeek locally on Apple Silicon using Ollama, with optional RAG workflows built with LangChain and ChromaDB.

## Overview

- Local LLM inference with no external API dependency
- Streamlit UI for interactive use
- RAG pipeline for PDF-based question answering

## Project Files

- `app.py`: Streamlit application
- `rag.py`: RAG pipeline logic
- `rag.ipynb`: Notebook workflow
- `requirements.txt`: Python dependencies

## Requirements

- Apple Silicon Mac (M1, M2, or M3)
- macOS 13+
- Python 3.9+
- Ollama installed and running

## Quick Start

1. Install Python dependencies:

```bash
python -m pip install -r requirements.txt
```

2. Pull a DeepSeek model in Ollama:

```bash
ollama pull deepseek-r1:1.5b
```

3. Run the Streamlit app:

```bash
streamlit run app.py
```

## RAG Pipeline Summary

The RAG flow in this project follows these steps:

1. Load PDF text (PyMuPDF)
2. Split text into chunks
3. Create embeddings with Ollama
4. Store vectors in ChromaDB
5. Retrieve relevant context for prompts
6. Generate responses with DeepSeek

## Example Local API Usage

```python
import ollama

response = ollama.chat(
    model="deepseek-r1:1.5b",
    messages=[{"role": "user", "content": "Explain Newton's second law."}],
)

print(response["message"]["content"])
```

## Troubleshooting

- Slow response: try a smaller model or reduce context size.
- Memory pressure: reduce chunk count or chunk size in the RAG pipeline.
- Missing model error: verify model availability with `ollama list`.

## Notes

- Vector store size grows with document volume.
- Keep an eye on available RAM and disk when indexing large PDFs.
