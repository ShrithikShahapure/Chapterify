from extract_transcript import  extract_transcript
from palm_api_summary import palm_api_summary
import streamlit as st

#passes video link to extract transcript and generate Youtube Chapters using Google PaLM

def extract_summary(video_link):
    video_transcript = extract_transcript(video_link)
    summary = palm_api_summary(video_transcript)
    st.success('Done!')
    st.write(summary)
