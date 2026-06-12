from app.agent.orchestrator import run_agent

question = input("Enter question: ")

response = run_agent(question)

print("\nResponse:")
print(response)