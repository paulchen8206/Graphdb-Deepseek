import ollama
import gradio as gr
import re
import os
import shutil
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma

import tempfile


def process_pdf(pdf_path):
    if not pdf_path:
        return None, None, None

    loader = PyMuPDFLoader(pdf_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = text_splitter.split_documents(documents)

    embeddings = OllamaEmbeddings(model="deepseek-r1:1.5b")

    temp_dir = tempfile.mkdtemp()
    vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=temp_dir)
    retriever = vectorstore.as_retriever()

    # Optionally, you can remove temp_dir after processing (or let the OS clean it up)
    # shutil.rmtree(temp_dir)  # Uncomment if you want immediate cleanup

    return text_splitter, vectorstore, retriever


def combine_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def ollama_llm(question, context):
    formatted_prompt = f"Question: {question}\n\nContext: {context}"
    response = ollama.chat(model="deepseek-r1:1.5b", messages=[{"role": "user", "content": formatted_prompt}])

    # Clean up response
    response_content = response["message"]["content"]
    final_answer = re.sub(r"<think>.*?</think>", "", response_content, flags=re.DOTALL).strip()
    return final_answer


def rag_chain(question, retriever):
    retrieved_docs = retriever.invoke(question)
    if not retrieved_docs:
        return "No relevant information found in the document."

    formatted_content = combine_docs(retrieved_docs)
    return ollama_llm(question, formatted_content)


def ask_question(pdf_file, question):
    """Handles PDF processing and answering user questions."""
    if pdf_file is not None:
        try:
            temp_pdf_path = pdf_file.name
            if not os.path.exists(temp_pdf_path):
                return "Error: File not found."

            _, _, retriever = process_pdf(temp_pdf_path)
            answer = rag_chain(question, retriever)
            return answer

        except Exception as e:
            return f"Error: {str(e)}"

        finally:
            if os.path.exists("./chroma_db"):
                shutil.rmtree("./chroma_db")
    else:
        return "Please upload a PDF to get document-based answers."


interface = gr.Interface(
    fn=ask_question,
    inputs=[
        gr.File(label="Upload PDF (optional)"),
        gr.Textbox(label="Question", placeholder="Type your question here..."),
    ],
    outputs="text",
    title="Ask a Question About a PDF",
    description="Upload a PDF and ask questions about its content.",
)

interface.launch()
