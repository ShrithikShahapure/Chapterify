from extract_chapters import extract_chapters
from extract_summary import extract_summary


import streamlit as st

st.header('Chapterify')

st.subheader('The one stop to Chapter Generation for Youtube ')

video_link = st.text_input('Please enter the link of your youtube video:')


col1, col2 = st.columns(2)
# Add a button to the first column
if col1.button('Generate Chapters'):
    extract_chapters(video_link)

# Add a button to the second column
if col2.button('Generate Summary'):
    extract_summary(video_link)

#functions work now
#divide the functions into seperate modules
#make different functions for both summary and generating chapters



    
