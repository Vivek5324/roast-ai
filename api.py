import os
import google.generativeai as genai
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

# Load environment variables
load_dotenv()

# Configure Gemini API
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("Missing API key! Set GOOGLE_API_KEY in .env file.")

genai.configure(api_key=API_KEY)

# FastAPI app
app = FastAPI()

# Request model
class ChatRequest(BaseModel):
    message: str

# Chat endpoint
@app.post("/chat")
async def chat(request: ChatRequest):
    response = genai.chat(messages=[{"role": "user", "content": request.message}])
    return {"reply": response["choices"][0]["message"]["content"]}
