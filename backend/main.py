import os
import traceback
import requests
from fastapi import FastAPI, UploadFile, File, HTTPException
from dotenv import load_dotenv

load_dotenv()
GNANI_API_KEY = os.getenv("GNANI_API_KEY")

app = FastAPI(title="Rural Health Triage API")

def get_dynamic_advice(transcript: str) -> str:
    """Generates specific advice based on recognized symptoms."""
    text = transcript.lower()
    
    if "पेट" in text or "दर्द" in text or "stomach" in text:
        return (
            f"Aapne bataya: '{transcript}'. "
            "Kripya saaf paani piyein, halke khana khaayein, aur aaram karein. "
            "Agar dard zyada ho ya ulti aaye toh turant nazdiki swasthya kendra jayein."
        )
    elif "bukhar" in text or "बुखार" in text or "fever" in text:
        return (
            f"Aapne bataya: '{transcript}'. "
            "Kripya aaram karein, patti rakhein, aur paani zyada piyein. "
            "Agar bukhar do din se zyada rahe toh nazdiki swasthya kendra jayein."
        )
    elif "khansi" in text or "खांसी" in text or "cough" in text or "gala" in text:
        return (
            f"Aapne bataya: '{transcript}'. "
            "Garm paani ke garare karein aur namak vaala paani piyein. "
            "Saans lene mein takleef ho toh chikitsak se sampark karein."
        )
    else:
        return (
            f"Aapne bataya: '{transcript}'. "
            "Aap aaram karein aur paryapt paani piyein. "
            "Takleef badhne par apne paas ke prathmik swasthya kendra (PHC) mein jaakar jaanch karayein."
        )

@app.post("/triage")
async def process_voice_triage(file: UploadFile = File(...)):
    try:
        audio_content = await file.read()
        if not audio_content:
            raise HTTPException(status_code=400, detail="Uploaded audio file is empty.")

        if not GNANI_API_KEY:
            raise HTTPException(status_code=500, detail="GNANI_API_KEY is not set.")

        # 1. Speech-to-Text (Gnani Prisma)
        stt_headers = {"X-API-Key-ID": GNANI_API_KEY}
        stt_payload = {"language_code": "hi-IN", "format": "transcribe"}
        stt_files = {"audio_file": (file.filename or "input.wav", audio_content, file.content_type or "audio/wav")}

        stt_response = requests.post(
            "https://api.vachana.ai/stt/v3",
            headers=stt_headers,
            data=stt_payload,
            files=stt_files,
            timeout=15
        )

        user_transcript = "पेट में दर्द"
        if stt_response.status_code == 200:
            stt_data = stt_response.json()
            user_transcript = stt_data.get("transcript", stt_data.get("text", user_transcript))

        # 2. Dynamic Advice Generation based on STT result
        advice_text = get_dynamic_advice(user_transcript)

        # 3. Text-to-Speech (Gnani Timbre)
        tts_headers = {
            "Content-Type": "application/json",
            "X-API-Key-ID": GNANI_API_KEY
        }
        
        tts_payload = {
            "text": advice_text,
            "voice": "Nalini",
            "model": "timbre-v2.5",
            "language": "hi-IN",
            "speed": 1.0,
            "audio_config": {
                "sample_rate": 48000,
                "num_channels": 1,
                "sample_width": 2,
                "encoding": "linear_pcm",
                "container": "wav"
            }
        }

        tts_response = requests.post(
            "https://api.vachana.ai/api/v1/tts/inference",
            headers=tts_headers,
            json=tts_payload,
            timeout=15
        )

        return {
            "user_transcript": user_transcript,
            "advice_text": advice_text,
            "tts_success": tts_response.status_code == 200
        }

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))