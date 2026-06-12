from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile"
)


def generate_explanation(question, context):

    prompt = f"""
You are a climate scientist.

Question:
{question}

Context:
{context}

Provide a detailed explanation using the context.
"""

    response = llm.invoke(prompt)

    return response.content