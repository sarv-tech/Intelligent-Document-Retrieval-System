import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama


st.set_page_config(
    page_title="NoteBot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 NoteBot AI")
st.caption("Upload notes and ask questions instantly")

with st.sidebar:
    st.title("📚 My Notes")

    # Upload multiple PDF files
    files = st.file_uploader(
        "Upload PDFs",
        type=["pdf"],
        accept_multiple_files=True
    )

# Store extracted text
all_text = ""

if files:

    st.success("✅ PDFs Uploaded Successfully")

    st.info(
        f"📄 Total Files: {len(files)}"
    )

    # Loop through uploaded PDFs
    for file in files:

        size = file.size

        # Show size in KB
        if size < 1024 * 1024:

            st.write(
                f"📘 {file.name} ({size / 1024:.2f} KB)"
            )

        else:
            st.write(
                f"📘 {file.name} ({size / (1024 * 1024):.2f} MB)"
            )

        # Read PDF
        pdf_reader = PdfReader(file)

        # Read all pages
        for page in pdf_reader.pages:

            # Extract text
            text = page.extract_text()

            # Store text
            if text:
                all_text += text

# SHOW EXTRACTED TEXT
if all_text:
    st.subheader("📄 Extracted Text")

    with st.expander("View Text"):
        st.write(all_text)

    # CHUNKING
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50,
        length_function=len
    )

    # Create chunks
    chunks = splitter.split_text(all_text)

    st.success("✅ Chunking Completed")

    st.info(
        f"✂️ Total Chunks: {len(chunks)}"
    )

    # Show chunks
    for i, chunk in enumerate(chunks):
        with st.expander(f"Chunk {i + 1}"):
            st.write(chunk)

    with st.spinner("Creating Embeddings..."):

        # Create Ollama embeddings
        embeddings = OllamaEmbeddings(

            # Recommended embedding model
            model="nomic-embed-text"
        )

        # Store vectors inside FAISS
        vector_store = FAISS.from_texts(
            chunks,
            embeddings
        )

    st.success("✅ Vector Store Created Successfully")

    # get user query
    user_query = st.chat_input(
        "Ask question from your notes..."
    )

    # semantic search from vector store
    if user_query:
        matching_chunks = vector_store.similarity_search(user_query, k=2)

        # define our LLM
        llm = ChatOllama(

            # Ollama model name
            model="phi3:mini",
            num_ctx=768,

            # Controls randomness
            temperature=0.1
        )

        # Convert matching chunks into context
        context = "\n\n".join(
            [doc.page_content for doc in matching_chunks]
        )

        # Create prompt
        prompt = f"""
        You are a professional AI assistant and personal learning tutor.

        Your role is to help the user understand concepts from their uploaded notes in a simple, clear, and structured way.

        RULES:
        - Use ONLY the provided context from uploaded documents.
        - Do NOT use external knowledge or assumptions.
        - If the answer is NOT present in the context, respond exactly:
          "I don't know. The information is not available in the provided notes."
        - Act as a helpful tutor: explain concepts in a simple and beginner-friendly way.
        - Break complex topics into step-by-step explanations when needed.
        - Keep responses concise, structured, and easy to understand.
        - Maintain a professional, supportive, and educational tone.
        - If the context is not sufficient to answer the question, respond exactly:
          "I don't know Sarvesh Pingale. The information is not available in the provided notes."

        CONTEXT:
        {context[:1500]}

        QUESTION:
        {user_query}

        FINAL ANSWER:
        """

        # Generate answer
        response = llm.invoke(prompt)

        # Show AI response
        st.subheader("🤖 AI Answer")

        st.write(response.content)
