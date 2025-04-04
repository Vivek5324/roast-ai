# AI Roast Battle 🔥

An interactive web application where users can engage in a roast battle with an AI powered by Gemini API.

## Backend Structure
```bash
backend/
├── app.py         # Flask application
├── chat.py        # Gemini AI integration
├── wsgi.py        # WSGI entry point
├── requirements.txt
└── runtime.txt
```

## Features
- Dark themed modern UI
- Three roast levels: Kid-friendly, Adult, and Dark humor
- Real-time AI responses
- Roast rating system

## Setup
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up Gemini API key in environment variables: `GEMINI_API_KEY`
4. Run the application: `python wsgi.py`

## API Endpoints
- POST `/roast`
  - Request body: `{ "name": string, "comeback": string, "level": string }`
  - Response: `{ "rating": string, "roast": string }`

## Deployment
- Backend: Deployed on Render
- API URL: https://roast-ai.onrender.com

## Technologies Used
- Python/Flask
- Gemini AI API
- HTML/CSS/JavaScript
- Async/Await for API calls

## Created by
BL4Z3 🔥 