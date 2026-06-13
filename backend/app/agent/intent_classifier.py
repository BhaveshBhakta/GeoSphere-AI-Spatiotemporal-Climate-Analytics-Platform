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
- current weather conditions
- current temperature
- humidity
- rainfall
- wind speed
- AQI values

prediction
- future weather
- tomorrow
- next week
- forecast
- prediction

analytics
- historical trends
- climate history
- past weather patterns
- over time analysis

risk
- danger assessment
- safety assessment
- heatwave risk
- flood risk
- drought risk
- air quality risk
- climate risk
- "Is it safe?"
- "Should I go outside?"
- "Should I avoid outdoor activities?"
- "How dangerous is it?"
- health impacts
- exposure risk

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