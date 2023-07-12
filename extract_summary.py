from extract_video_id import  extract_transcript
from open_ai_summary import open_ai_summary
import streamlit as st
def extract_summary(video_link):
    video_transcript = extract_transcript(video_link)
    summary = open_ai_summary(video_transcript)
    st.write(summary)