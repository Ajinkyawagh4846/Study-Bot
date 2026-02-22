# Study Bot 🤖

An AI-powered Study Assistant chatbot built with FastAPI, LangChain, Groq, and MongoDB.

## Features
- Ask any study/academic questions
- Remembers previous conversations using MongoDB
- REST API built with FastAPI

## Endpoints
- `GET /` - Check if API is running
- `POST /chat` - Send a message to the bot
- `GET /history/{user_id}` - Get chat history

## Setup
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Create `.env` file with your keys
4. Run: `uvicorn main:app --reload`
