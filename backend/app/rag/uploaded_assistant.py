from langchain_chroma import (
    Chroma
)

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from langchain_groq import (
    ChatGroq
)


def ask_uploaded_pdf(
    question
):

    embeddings = (
        HuggingFaceEmbeddings(
            model_name=
            "sentence-transformers/all-MiniLM-L6-v2"
        )
    )

    vectordb = Chroma(

        collection_name=
        "uploaded_climate_docs",

        persist_directory=
        "chroma_db",

        embedding_function=
        embeddings
    )

    docs = vectordb.similarity_search(
        question,
        k=5
    )

    context = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )

    llm = ChatGroq(
        model_name=
        "llama-3.3-70b-versatile"
    )

    prompt = f"""
Answer using the uploaded PDF.

Question:
{question}

Context:
{context}
"""

    response = llm.invoke(
        prompt
    )

    return response.content