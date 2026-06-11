from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from langchain_chroma import Chroma


CHROMA_PATH = "app/rag/chroma_db"


embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embedding_model
)


retriever = vectorstore.as_retriever(
    search_kwargs={"k": 4}
)