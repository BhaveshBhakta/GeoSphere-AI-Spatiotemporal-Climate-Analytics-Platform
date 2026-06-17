from langchain_community.document_loaders import (
    PyPDFLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from langchain_chroma import (
    Chroma
)


def ingest_uploaded_pdf(
    pdf_path
):

    loader = PyPDFLoader(
        pdf_path
    )

    documents = loader.load()

    splitter = (
        RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
    )

    chunks = splitter.split_documents(
        documents
    )

    embeddings = (
        HuggingFaceEmbeddings(
            model_name=
            "sentence-transformers/all-MiniLM-L6-v2"
        )
    )

    vectordb = Chroma(

        collection_name=
        "uploaded_climate_docs",

        embedding_function=
        embeddings,

        persist_directory=
        "chroma_db"
    )

    vectordb.add_documents(
        chunks
    )

    return len(chunks)