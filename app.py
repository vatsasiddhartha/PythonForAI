import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from google import genai


MODEL = "gemini-3.6-flash"
load_dotenv(Path(__file__).parent / ".venv" / ".env")

DEFAULT_PROMPT = (
    "Create a practical roadmap for me to learn AI engineering and machine learning. "
    "Assume I am a beginner and can study 8 hours per week. "
    "Include weekly milestones, topics to learn, and hands-on projects."
)

st.set_page_config(page_title="AI Roadmap Generator", page_icon="🧭")
st.title("AI Roadmap Generator")
st.write("Describe your goal and experience, and Gemini will create a learning roadmap.")

prompt = st.text_area(
    "What roadmap do you want?",
    value=DEFAULT_PROMPT,
    height=150,
)

if st.button("Generate roadmap", type="primary"):
    st.session_state.pop("roadmap_result", None)
    if not prompt.strip():
        st.error("Enter a request for your roadmap.")
    else:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            st.error("GEMINI_API_KEY was not found. Add it to .venv/.env or set it in your environment.")
        else:
            with st.spinner("Generating your roadmap..."):
                client = genai.Client(api_key=api_key)
                response = client.models.generate_content(
                    model=MODEL,
                    contents=prompt,
                )
            if response.text:
                st.session_state["roadmap_result"] = response.text
            else:
                st.warning("Gemini returned an empty response. Try changing your request.")

if "roadmap_result" in st.session_state:
    st.subheader("Your roadmap")
    st.markdown(st.session_state["roadmap_result"])
