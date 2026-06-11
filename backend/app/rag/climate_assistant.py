from app.rag.retriever import retriever

from app.rag.groq_chain import llm


def ask_climate_assistant(question):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are a climate science expert.

Answer only from the provided context.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content