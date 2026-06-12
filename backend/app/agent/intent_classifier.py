from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile"
)


def classify_intent(question):

    prompt = f"""
You are an intent classification system.

Classify the user question into EXACTLY ONE category.

Categories:

rag
- climate science concepts
- climate change
- greenhouse gases
- global warming
- sustainability
- environmental science
- explanations from climate reports

weather
- current weather
- temperature today
- humidity
- rainfall
- wind
- AQI
- weather conditions

prediction
- future weather
- tomorrow
- forecast
- predict
- next week

analytics
- historical trends
- history
- over time
- past climate data

risk
- drought risk
- flood risk
- heatwave risk
- climate risk

Question:
{question}

Return ONLY one word:

rag
weather
prediction
analytics
risk
"""

    response = llm.invoke(prompt)

    return response.content.strip().lower()