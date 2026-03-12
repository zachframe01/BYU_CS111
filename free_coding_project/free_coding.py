#gemini api Key:
# AIzaSyBVLy_WKV-5YpFTcR26WGYrHktSv-Wz1rU


import streamlit as st
from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi

# --- CONFIGURATION (The "Swap" Area) ---
# To use Gemini directly:
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
MODEL_NAME = "gemini-2.0-flash" # Use Flash for speed/testing

# To use OpenRouter later, you'd just change these to:
# BASE_URL = "https://openrouter.ai/api/v1"
# MODEL_NAME = "anthropic/claude-3.5-sonnet"
# ---------------------------------------

st.set_page_config(page_title="Sub-Tube Digest", page_icon="📺")
st.title("📺 The YouTube Digest")
st.subheader("Turn YouTube noise into readable newsletters.")

# Sidebar for API Key
with st.sidebar:
    api_key = st.text_input("Enter your Gemini API Key", type="password")
    st.info("Your key stays in this session and isn't stored.")

# Main UI
video_url = st.text_input("Paste a YouTube Video URL:")

if st.button("Generate Summary"):
    if not api_key:
        st.error("Please enter an API key in the sidebar!")
    elif "v=" not in video_url:
        st.error("Please enter a valid YouTube URL (e.g., youtube.com/watch?v=...)")
    else:
        try:
            # 1. Extract Video ID
            video_id = video_url.split("v=")[1].split("&")[0]
            
            with st.spinner("Fetching transcript..."):
                # 2. Get Transcript
                transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
                full_text = " ".join([t['text'] for t in transcript_data])
            
            with st.spinner("AI is reading the script..."):
                # 3. Setup the Universal Client
                client = OpenAI(api_key=api_key, base_url=BASE_URL)
                
                # 4. Generate Summary
                response = client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=[
                        {"role": "system", "content": "You are a professional editor for a tech newsletter like Substack. Summarize the following transcript into a catchy title, a TL;DR section, and 3 key takeaways using bullet points."},
                        {"role": "user", "content": full_text}
                    ]
                )
                
                # 5. Display Result
                st.markdown("---")
                st.markdown(response.choices[0].message.content)
                
        except Exception as e:
            st.error(f"An error occurred: {e}")