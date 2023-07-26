from extract_transcript import  extract_transcript
from palm_api_chapters import  palm_api_chapters
import streamlit as st

#passes video link to extract transcript and generate Youtube Chapters using Google PaLM
def extract_chapters(video_link):
    video_transcript = extract_transcript(video_link)
    chapters = palm_api_chapters(video_transcript)
    st.success('Done!')
    st.write(chapters)
