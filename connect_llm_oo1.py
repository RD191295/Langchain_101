from langchain_groq import ChatGroq
from dotenv import load_dotenv,find_dotenv
import os

_ = load_dotenv(find_dotenv())

# Load the environment variables
groq_api = os.getenv("GROP_API_KEY")

chat_groq_model = ChatGroq(
    model='llama-3.1-70b-versatile',
    api_key = groq_api,
    temperature= 0.7,
    max_retries=3,
)

messages = [
    (
        "system",
        "You are a software devloper expert who know software design concept.",
    ),
    ("human", "Tell me one curious thing about JFK"),
]

for chunk in chat_groq_model.stream(messages):
    print(chunk.content, end = "")
