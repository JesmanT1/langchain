from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Replace with your actual API key
api_key = "AIzaSyDiPn4HyhWSG4a7TmIV1kujCGPMYQWVNfM"

# Initialize the Gemini 1.5 Flash model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)

# Get user input
user_message = input("Enter your message: ")

# Define the message
messages = [HumanMessage(content=user_message)]

# Invoke the LLM and print the response
response = llm.invoke(messages)
print(response.content)