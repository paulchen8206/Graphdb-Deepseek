import streamlit as st
import ollama
import re
import os
import shutil
import tempfile
import time

from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
#from langchain_community.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

def process_pdf(pdf_path):
    """
    Processes the PDF file:
      - Loads and splits text into chunks.
      - Checks that at least one non-empty chunk was extracted.
      - Creates embeddings and builds a vectorstore using a temporary directory.
    Returns the text splitter, vectorstore, retriever, and the temporary directory.
    """
    if not pdf_path:
        return None, None, None, None

    loader = PyMuPDFLoader(pdf_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = text_splitter.split_documents(documents)

    if not chunks or all(not doc.page_content.strip() for doc in chunks):
        raise ValueError("No text found in the PDF file. Please upload a PDF with searchable text.")

    embeddings = OllamaEmbeddings(model="deepseek-r1:1.5b")

    temp_dir = tempfile.mkdtemp()
    vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=temp_dir)
    retriever = vectorstore.as_retriever()

    return text_splitter, vectorstore, retriever, temp_dir


def combine_docs(docs):
    """Combine document chunks into a single string."""
    return "\n\n".join(doc.page_content for doc in docs)


def ollama_llm(question, context):
    """
    Uses the Ollama model to generate an answer based on the provided question and context.
    Extracts "thinking" sections enclosed in <think> tags.
    """
    formatted_prompt = f"Question: {question}\n\nContext: {context}"
    response = ollama.chat(model="deepseek-r1:1.5b", messages=[{"role": "user", "content": formatted_prompt}])
    full_output = response["message"]["content"]

    matches = re.findall(r"<think>(.*?)</think>", full_output, flags=re.DOTALL)
    chain_of_thought = "\n\n".join(match.strip() for match in matches) if matches else None

    final_answer = re.sub(r"<think>.*?</think>", "", full_output, flags=re.DOTALL).strip()

    return final_answer, chain_of_thought


def rag_chain(question, retriever):
    """Retrieve relevant chunks and generate an answer using the LLM."""
    retrieved_docs = retriever.invoke(question)
    if not retrieved_docs:
        return "No relevant information found in the document.", None
    formatted_content = combine_docs(retrieved_docs)
    return ollama_llm(question, formatted_content)


def ask_question(pdf_file, question):
    """
    Handles PDF processing and answering the user's question.
    Returns a tuple containing the final answer and the chain-of-thought.
    """
    if pdf_file is None:
        return "Please upload a PDF to get document-based answers.", None

    tmp_path = None
    temp_dir = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(pdf_file.read())
            tmp_path = tmp.name

        _, _, retriever, temp_dir = process_pdf(tmp_path)
        answer, chain_of_thought = rag_chain(question, retriever)
        return answer, chain_of_thought

    except Exception as e:
        return f"Error: {str(e)}", None

    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.remove(tmp_path)
        if temp_dir and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)


def clear_memory():
    """Clears session state and refreshes the page."""
    if os.path.exists("./chroma_db"):
        shutil.rmtree("./chroma_db")
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.success("Memory cleared! Refreshing page...")
    st.markdown(
        """
        <script>
        setTimeout(function(){
            window.location.reload();
        }, 1000);
        </script>
        """,
        unsafe_allow_html=True,
    )


def main():
    # --- Custom CSS for a prettier UI ---
    st.markdown(
        """
        <style>
        .main-container {
            background-color: #F9F9F9;
            padding: 2rem;
            border-radius: 8px;
            max-width: 800px;
            margin: auto;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #333333;
        }
        .clear-btn {
            float: right;
            margin-bottom: 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.title("📄 PDF Insight Explorer")
    st.write("Upload a PDF and ask questions about its content.")

    if st.button("🧹 Clear Memory", key="clear_btn"):
        clear_memory()

    pdf_file = st.file_uploader("Upload PDF", type=["pdf"])
    question = st.text_area("Your Question", placeholder="Type your question here...")

    if st.button("🚀 Ask Question"):
        if not question:
            st.warning("⚠️ Please enter a question.")
        else:
            with st.spinner("🔍 Analyzing document and generating answer..."):
                answer, chain_of_thought = ask_question(pdf_file, question)

            st.subheader("🧠 Chain-of-Thought Reasoning")
            st.write(chain_of_thought if chain_of_thought else "No chain-of-thought available.")

            st.subheader("💡 Answer")
            final_answer_container = st.empty()
            streaming_text = ""
            for chunk in [answer[i : i + 50] for i in range(0, len(answer), 50)]:
                streaming_text += chunk
                final_answer_container.markdown(streaming_text)
                time.sleep(0.1)

    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
