from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import os

PDF_FOLDER = "app/rag/documents"

CHROMA_PATH = "app/rag/chroma_db"

documents = []

for file in os.listdir(PDF_FOLDER):

    if file.endswith(".pdf"):

        loader = PyPDFLoader(
            os.path.join(PDF_FOLDER, file)
        )

        documents.extend(
            loader.load()
        )


splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(
    documents
)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory=CHROMA_PATH
)

print(
    f"Stored {len(chunks)} chunks"
)