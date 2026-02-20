from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from pymongo import MongoClient
import os

# ─────────────────────────────────────────
# 1. Load environment variables from .env
# ─────────────────────────────────────────
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MONGO_URI = os.getenv("MONGO_URI")

# ─────────────────────────────────────────
# 2. Connect to MongoDB
# ─────────────────────────────────────────
client = MongoClient(MONGO_URI)
db = client["studybot"]           # Database name: studybot
collection = db["chat_history"]   # Collection name: chat_history

# ─────────────────────────────────────────
# 3. Connect to Groq LLM (AI Model)
# ─────────────────────────────────────────
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile"   # Free and fast model from Groq
)

# ─────────────────────────────────────────
# 4. Create FastAPI app
# ─────────────────────────────────────────
app = FastAPI()

# ─────────────────────────────────────────
# 5. Define what a chat request looks like
# ─────────────────────────────────────────
class ChatRequest(BaseModel):
    user_id: str    # To identify which user is chatting
    message: str    # The user's question

# ─────────────────────────────────────────
# 6. System Prompt (makes bot behave like a Study Assistant)
# ─────────────────────────────────────────
SYSTEM_PROMPT = """You are Study Bot, a helpful AI study assistant. 
You help students understand academic topics clearly and simply.
You can explain concepts, answer questions, and help with learning.
Always be encouraging, patient, and educational in your responses."""

# ─────────────────────────────────────────
# 7. Main Chat Endpoint
# ─────────────────────────────────────────
@app.post("/chat")
def chat(request: ChatRequest):

    # Step A: Load this user's previous chat history from MongoDB
    history = list(collection.find({"user_id": request.user_id}))

    # Step B: Build the message list to send to the AI
    messages = [SystemMessage(content=SYSTEM_PROMPT)]  # Always start with system prompt

    for entry in history:
        messages.append(HumanMessage(content=entry["user_message"]))
        messages.append(AIMessage(content=entry["bot_response"]))

    # Step C: Add the new user message
    messages.append(HumanMessage(content=request.message))

    # Step D: Send to Groq and get response
    response = llm.invoke(messages)
    bot_reply = response.content

    # Step E: Save the new conversation to MongoDB
    collection.insert_one({
        "user_id": request.user_id,
        "user_message": request.message,
        "bot_response": bot_reply
    })

    # Step F: Return the response
    return {
        "user_id": request.user_id,
        "user_message": request.message,
        "bot_response": bot_reply
    }

# ─────────────────────────────────────────
# 8. History Endpoint (see past conversations)
# ─────────────────────────────────────────
@app.get("/history/{user_id}")
def get_history(user_id: str):
    history = list(collection.find({"user_id": user_id}, {"_id": 0}))
    return {"user_id": user_id, "history": history}

# ─────────────────────────────────────────
# 9. Home route (just to test if API is running)
# ─────────────────────────────────────────
@app.get("/")
def home():
    return {"message": "Study Bot is running! Go to /docs to test the API."}