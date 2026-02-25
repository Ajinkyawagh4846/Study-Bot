# 🤖 Study Bot — AI-Powered Study Assistant

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-121212?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Groq-FF6B00?style=for-the-badge" />
</p>

> An intelligent AI-powered chatbot that helps students learn by answering academic questions — and remembers every conversation using MongoDB.

---

## 📖 About the Project

The **Study Bot** is a REST API-based AI study assistant built as part of the Devtown AI Workshop project. It leverages large language models (LLMs) via the Groq API to provide fast, intelligent responses to student questions across any academic subject.

What makes it special is its **memory system** — every conversation is stored in MongoDB, so the bot remembers what you've previously discussed and gives context-aware responses, just like a real tutor would.

---

## ✨ Features

- 🧠 **AI-Powered Responses** — Uses Groq's LLM (llama-3.3-70b) for fast, accurate answers
- 💾 **Persistent Memory** — Stores full chat history in MongoDB
- 🎯 **Context-Aware** — Remembers previous messages for follow-up questions
- 📚 **Study-Focused** — System prompt tuned specifically for academic assistance
- 🚀 **Fast API** — Built with FastAPI for high performance
- 📄 **Auto Docs** — Interactive Swagger UI available at `/docs`
- ☁️ **Cloud Deployed** — Hosted on Render

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **FastAPI** | Web framework & API creation |
| **Python 3.14** | Core programming language |
| **LangChain** | LLM orchestration framework |
| **Groq API** | LLM provider (llama-3.3-70b-versatile) |
| **MongoDB** | Chat history storage |
| **PyMongo** | MongoDB Python driver |
| **Uvicorn** | ASGI server |
| **Render** | Cloud deployment platform |

---

## 📁 Project Structure

```
study-bot/
│
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not pushed to GitHub)
├── .gitignore           # Git ignore rules
└── README.md            # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- MongoDB (local or Atlas)
- Groq API Key (free at [console.groq.com](https://console.groq.com))

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/Ajinkyawagh4846/Study-Bot.git
cd Study-Bot
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create a `.env` file**
```env
GROQ_API_KEY=your_groq_api_key_here
MONGO_URI=mongodb://localhost:27017
```

**5. Start MongoDB**
```bash
mongod --dbpath "D:\data\db"
```

**6. Run the application**
```bash
python -m uvicorn main:app --port 8000
```

**7. Open the API docs**
```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

### `GET /`
Check if the API is running.

**Response:**
```json
{
  "message": "Study Bot is running! Go to /docs to test the API."
}
```

---

### `POST /chat`
Send a message to the Study Bot.

**Request Body:**
```json
{
  "user_id": "student1",
  "message": "What is photosynthesis?"
}
```

**Response:**
```json
{
  "user_id": "student1",
  "user_message": "What is photosynthesis?",
  "bot_response": "Photosynthesis is the process by which plants use sunlight, water, and carbon dioxide to produce oxygen and energy in the form of glucose..."
}
```

---

### `GET /history/{user_id}`
Retrieve the full chat history for a specific user.

**Example:** `GET /history/student1`

**Response:**
```json
{
  "user_id": "student1",
  "history": [
    {
      "user_id": "student1",
      "user_message": "What is photosynthesis?",
      "bot_response": "Photosynthesis is..."
    }
  ]
}
```

---

## 🧠 How Memory Works

```
User sends message
        ↓
Load previous messages from MongoDB (for this user_id)
        ↓
Build full conversation history → [System Prompt + Past Messages + New Message]
        ↓
Send to Groq LLM → Get intelligent, context-aware response
        ↓
Save new message + response to MongoDB
        ↓
Return response to user
```

This means if you ask "What is Newton's First Law?" and then follow up with "Can you give me an example?", the bot knows exactly what you're referring to — because it remembers the conversation.

---

## ☁️ Deployment

This project is deployed on **Render**.

**Live API:** `[https://ai-study-bot-u4tt.onrender.com/]`

**Environment variables set on Render:**
- `GROQ_API_KEY` — Groq API key
- `MONGO_URI` — MongoDB Atlas connection string

**Start command used:**
```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

## 👨‍💻 Author

**Ajinkya Wagh**  
Built as part of the **Devtown AI Development Workshop**

