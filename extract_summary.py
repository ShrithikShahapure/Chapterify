from extract_transcript import  extract_transcript
from open_ai_summary import open_ai_summary
import streamlit as st
import pyperclip

#passes video link to extract transcript and generate Youtube Chapters using OpenAI

def extract_summary(video_link):
    video_transcript = extract_transcript(video_link)
    summary = open_ai_summary(video_transcript)
    st.success('Done! Added to clipboard.')
    pyperclip.copy(summary)         # use pyperclip to add the transcript to the clipboard automatically
    st.text(summary)