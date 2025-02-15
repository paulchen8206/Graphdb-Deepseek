# DeepSeek Local Inference with Ollama for Apple Silicon

A production-ready implementation for running DeepSeek language models locally on Apple Silicon, leveraging Metal acceleration through Ollama. This project implements a RAG (Retrieval-Augmented Generation) pipeline for document analysis with vector-based semantic search.

## Overview

This system enables local LLM inference using DeepSeek models, optimized for Apple Silicon architecture. It includes a RAG implementation using ChromaDB as the vector store, allowing for context-aware document analysis without external API dependencies.

## Key Features
- **Local Inference**: Full local execution on Apple Silicon using Metal acceleration
- **RAG Pipeline**: Document processing with semantic search via ChromaDB
- **Streaming Inference**: Real-time token streaming with visible reasoning steps
- **Resource Management**: Automatic memory cleanup and vector store persistence
- **Metal Optimization**: Leverages Apple's Metal API for GPU acceleration

## System Requirements

- Apple Silicon (M1/M2/M3) Mac
- macOS 13.0+ (Ventura or later)
- Python 3.9+
- 16GB+ RAM recommended

## Quick Start

1. Install dependencies:
```bash
python -m pip install -r requirements.txt
```

2. Launch the application:
```bash
streamlit run app.py
```

## **Install & import relevant packages**

To build a simple chatbot using Python, we need to install the following packages. Each package serves a specific purpose in our chatbot pipeline:

- **`ollama`**: This package allows us to run large language models (LLMs) locally. It simplifies interactions with models like LLaMA and Mistral.
- **`langchain`**: A framework for building applications powered by LLMs. It provides tools for chaining prompts, managing memory, and integrating models.
- **`chromadb`**: A vector database used for storing and retrieving text embeddings. This is essential for making the chatbot context-aware.
- **`gradio`**: A simple way to build web-based interfaces for machine learning models. We’ll use it to create a user-friendly chatbot interface.
- **`langchain-community`**: A collection of integrations and utilities that extend `langchain`, making it easier to work with external tools and databases.
- **`pymupdf`**: To work with PDF documents, we need to install `pymupdf` which makes it easy to handle PDF files. 

## Architecture

### Document Processing Pipeline
1. PDF ingestion via PyMuPDF
2. Chunk segmentation using recursive character splitting
3. Vector embedding generation
4. ChromaDB persistence layer


## **Install and Call DeepSeek R1 1.5B via API**

### Installation DeepSeek on Mac
#### Step 1: Download Ollama
To begin, you need to download Ollama:
1. Visit the Ollama official website
2. Locate the macOS download link
3. Save the installer

#### Step 2: Install Ollama on Your Mac
Once the download is complete, follow these steps to install Ollama:
1. Locate the downloaded installer
Go to your Downloads folder (or the location you saved the installer) and find the .dmg file.
2. Open the installer
Double-click the .dmg file to mount it. A window will pop up displaying the Ollama icon.
3. Drag the Ollama icon into the Applications folder
Drag the Ollama icon to your Applications folder. This installs Ollama on your Mac.
4. Launch Ollama
After installation, go to the Applications folder and double-click the Ollama icon to open it. You can also search for it using Spotlight.

#### Step 3: Download the DeepSeek Model
Now that Ollama is installed, you can download the DeepSeek model:
1. Open the Terminal
Use Spotlight to search for and open the Terminal app on your Mac.
2. Download the DeepSeek model
In the Terminal, type the following command to download the DeepSeek model:
ollama run deepseek-r1:1.5b
This will start downloading the model. Depending on your internet speed, the download may take a few minutes.

#### Step 4: Run DeepSeek
Once the model is downloaded, you can start using DeepSeek:
1. Run the model
In the Terminal, type the following command to initiate DeepSeek:
```bash
ollama run deepseek-r1:1.5b
```
This command will launch DeepSeek and start processing your inputs. You will see the model load and initialize in the Terminal.
2. Start interacting with the model

### Call DeepSeek R1 1.5B via API
we use `ollama.chat()` to generate a response from DeepSeek R1 1.5B (which is installed locally). Let’s break it down:

- **Choosing the Model**: We specify `"deepseek-r1:1.5b"` using the `model` argument.
- **Passing User Messages**: The `messages` parameter is a list of interactions, where each message contains:
  - `"role": "user"` – Indicates that the message is from the user.
  - `"content": "Explain Newton's second law of motion"` – The actual question asked.
- **Extracting and Printing the Response**: The model generates a structured response, where the content of the reply is stored in `response["message"]["content"]`. We print this output to display the answer.

## Preprocess the PDF Document for RAG

We will now create a function that pre-processes the PDF file for RAG. Below is a breakdown of its logic:

- **Check if a PDF is provided**: If no file is uploaded, the function returns `None`, preventing unnecessary processing.
- **Extract text from the PDF**: Uses `PyMuPDFLoader` to load and extract raw text from the document.
- **Split the text into chunks**: Since LLMs process smaller text fragments better, we use `RecursiveCharacterTextSplitter`. Each chunk contains **500 characters**, with an **overlap of 100 characters** to maintain context.
- **Generate embeddings for each chunk**: Uses `OllamaEmbeddings` with the `"deepseek-r1:1.5b"` model to convert text into **numerical vectors**. These embeddings allow us to find **meaning-based matches** rather than exact keyword searches.
- **Store embeddings in a vector database**: We use `ChromaDB` to **store and organize** the generated embeddings efficiently. The data is **persisted** in `"./chroma_db"` to avoid recomputing embeddings every time.
- **Create a retriever for searching the database**: The retriever acts like a **smart search engine**, enabling the chatbot to fetch the most relevant text when answering questions.
- **Return essential components**
    - `text_splitter` (for future text processing)
    - `vectorstore` (holding the document embeddings)
    - `retriever` (allowing AI-powered search over the document)

## **What are embeddings?**
Embeddings are **numerical representations of text** that capture meaning. Instead of treating words as just sequences of letters, embeddings transform them into **multi-dimensional vectors** where similar words or sentences **are placed closer together**.

![image](https://miro.medium.com/v2/resize:fit:1400/1*OEmWDt4eztOcm5pr2QbxfA.png)
_Source: https://medium.com/towards-data-science/word-embeddings-intuition-behind-the-vector-representation-of-the-words-7e4eb2410bba_

### **Intuition: how do embeddings work?**
Imagine a **map of words**:
- Words with **similar meanings** (*cat* and *dog*) are **closer together**.
- Words with **different meanings** (*cat* and *car*) are **farther apart**.
- Sentences or paragraphs with similar **context** will have embeddings that are **close to each other**.

This means when a user asks a question, the LLM doesn’t just look for **exact words**—it finds the **most relevant text based on meaning**, even if the wording is different.

### **Why this matters?**
This function enables a chatbot to **understand and retrieve information from PDFs efficiently**. Instead of simple keyword searches, it **finds contextually relevant information**, making AI responses **more accurate and useful**.


This approach allows us to interact with an LLM locally, making it a powerful way to answer queries without relying on external APIs.
### Inference Pipeline
1. Query embedding generation
2. Semantic search in vector space
3. Context assembly and prompt construction
4. Local inference via Ollama
5. Stream processing and response rendering

## Performance Considerations

- **Memory Usage**: Vector store size scales with document corpus
- **Inference Speed**: Dependent on chosen model quantization
- **Disk Usage**: ~4GB for base model, additional for vector store

## Troubleshooting

### Common Issues

1. **OOM Errors**
   - Reduce `MAX_CONTEXT_CHUNKS`
   - Use model quantization

2. **Slow Inference**
   - Verify Metal acceleration
   - Monitor thermal throttling
   - Consider lighter model variants

3. **Vector Store Issues**
   - Clear persistent storage
   - Rebuild index

## Acknowledgments
- Ollama Team for Metal optimization
- ChromaDB for vector store implementation
