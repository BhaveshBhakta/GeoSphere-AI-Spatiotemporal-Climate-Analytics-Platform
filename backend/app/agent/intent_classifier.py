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
- historical weather
- past weather patterns
- over time analysis
- trend analysis
- has temperature increased
- has climate changed
- historical climate risk
- long term climate trends

risk
- danger assessment
- safety assessment
- heatwave risk
- flood risk
- drought risk
- air quality risk
- climate risk
- health impacts
- exposure risk

Examples:
- Is Delhi safe today?
- Should I go outside?
- Is Delhi dangerous today?
- Is there a heatwave risk?
- Is air pollution dangerous?

analysis
- combine weather + risk + forecast + climate knowledge
- climate intelligence
- climate impact assessment
- climate challenges
- climate recommendations
- future climate risks
- complex reasoning requiring multiple tools

Examples:
- How will climate change affect Delhi?
- What are Delhi's biggest climate risks?
- Is Delhi becoming more dangerous due to climate change?
- What climate challenges will Delhi face in the future?
- How should Delhi prepare for climate change?

Question:
{question}

Return ONLY one word:

rag
weather
prediction
analytics
risk
analysis
"""

    response = llm.invoke(prompt)

    return response.content.strip().lower()