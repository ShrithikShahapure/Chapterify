from extract_video_id import  extract_transcript
from open_ai_chapters import  open_ai_chapters
import streamlit as st


def extract_chapters(video_link):
    video_transcript = extract_transcript(video_link)

    chapters = open_ai_chapters(video_transcript)
    st.write(chapters)