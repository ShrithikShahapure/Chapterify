from extract_transcript import  extract_transcript
from open_ai_chapters import  open_ai_chapters
import streamlit as st
import  pyperclip

#passes video link to extract transcript and generate Youtube Chapters using OpenAI
def extract_chapters(video_link):
    video_transcript = extract_transcript(video_link)
    chapters = open_ai_chapters(video_transcript)
    st.success('Done! Added to clipboard.')
    pyperclip.copy(chapters)            # use pyperclip to add the chapters to the clipboard automatically
    st.text(chapters)