🩺 Swasthya Vaani: Rural Health Voice Triage Assistant

An AI-powered voice-enabled healthcare triage application designed to bridge the healthcare accessibility gap in rural areas by allowing users to speak symptoms in regional languages and receive instant, structured medical guidance.

Built for the Great Indian AI Internship Challenge utilizing Gnani AI Models.

🚀 Key Features

Voice-First Interface: Record symptoms naturally via a microphone in local languages (Hindi/Hinglish).

Speech-to-Text (STT): Powered by Gnani Prisma v2.5 for high-accuracy regional language transcription.

Smart Medical Triage: Dynamic backend rules engine that analyzes symptoms and categorizes triage advice (e.g., stomach pain, fever, cough).

Text-to-Speech (TTS): Integrated with Gnani Timbre v2.5 for natural-sounding spoken audio output.

🛠️ Tech Stack

Frontend: Streamlit (frontend/app.py), audio-recorder-streamlit

Backend: FastAPI, Python, Uvicorn (backend/main.py)

AI APIs: Gnani AI Vachana APIs (Prisma & Timbre)

Environment Management: Python dotenv

## 📁 Project Directory Structure

```text
rural-health-voice/
├── .venv/
├── backend/
│   ├── __pycache__/
│   └── main.py          # FastAPI server & Gnani API integration logic
├── frontend/
│   └── app.py           # Streamlit user interface
├── .env                 # API keys (Keep private - do not commit)
└── README.md            # Project documentation
```


⚙️ Installation & Setup Guide

1. Clone the Repository

git clone https://github.com/pranjaljain062-cyber/rural-health-voice.git
cd rural-health-voice



2. Install Dependencies

pip install fastapi uvicorn streamlit audio-recorder-streamlit requests python-dotenv


3. Set Up Environment Variables

Create a file named .env in the root directory of your project and add your Gnani AI API key:

GNANI_API_KEY=vach_1ytE2CY5X2ESDxfuDLUzNl8EeHy5BHosIgFXDXhFuAixVpyVYRhQNdO6OwDLUwbSuMnOS7VgxSBPSi4XUQhKAzTzRDrj3PCH_77908bf042c8d65e5fe5da582ffb3ac8


🚀 Running the Application

You will need two separate terminal tabs to run the application locally.

Terminal 1: Start the FastAPI Backend

Make sure you are in the project root directory (rural-health-voice):

uvicorn backend.main:app --reload


(Backend runs on http://127.0.0.1:8000)

Terminal 2: Start the Streamlit Frontend

Navigate into the frontend directory and start Streamlit:

cd frontend
streamlit run app.py


(Frontend opens automatically in your browser at http://localhost:8501)

💡 Usage

Open the Streamlit web app in your browser.

Click the microphone button and state your symptoms (e.g., "Pet mein dard hai" or "Bukhar hai").

Click "Send to Health Assistant" to view the Prisma transcription and tailored triage advice.

🏆 Submission Note

Developed as part of the Great Indian AI Internship Challenge, showcasing real-world integration of conversational voice AI APIs for social impact.
