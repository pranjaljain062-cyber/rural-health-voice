import streamlit as st
import requests
from audio_recorder_streamlit import audio_recorder

st.set_page_config(page_title="Rural Health Voice Triage", page_icon="🩺")

st.title("🩺 Swasthya Vaani - Rural Health Voice Triage")
st.write("Speak your symptoms in Hindi or Hinglish, and get instant guidance!")

st.divider()

st.subheader("1. Record Your Symptoms")
audio_bytes = audio_recorder(
    text="Click to Record Audio",
    recording_color="#e8b62c",
    neutral_color="#6aa36f",
    icon_name="microphone",
    icon_size="3x",
)

if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")
    
    if st.button("Send to Health Assistant 🚀"):
        with st.spinner("Processing speech via Gnani Prisma & Timbre..."):
            try:
                files = {"file": ("recording.wav", audio_bytes, "audio/wav")}
                response = requests.post("http://127.0.0.1:8000/triage", files=files)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    st.success("Analysis Complete!")
                    st.divider()
                    
                    st.subheader("2. Results & Advice")
                    st.markdown(f"**What we heard (Prisma STT):**\n> *{data.get('user_transcript')}*")
                    st.markdown(f"**Triage Advice:**\n{data.get('advice_text')}")
                    
                    if data.get("tts_success"):
                        st.info("🔊 Timbre Text-to-Speech audio successfully generated and synthesized!")
                else:
                    st.error(f"Backend error: {response.status_code}")
            except Exception as e:
                st.error(f"Connection failed: {e}")