from extract_chapters import extract_chapters
from extract_summary import extract_summary
import streamlit as st

st.set_page_config(page_title='Chapterify',
                   page_icon="chapterify_icon.webp",
                   menu_items={
                        'Get Help': 'https://github.com/ShrithikShahapure/Chapterify',
                        'Report a bug': "https://github.com/ShrithikShahapure/Chapterify",
                        'About': '''## Chapterify
                        
                        Generate Chapters and summaries for youtube videos'''
                   }
                   )
#meta information
st.markdown(
    """
    <head>
        <!-- Meta tags -->
        <meta name="description"Chapterify: Generate Chapters and summaries for youtube videos">
        <meta name="keywords" content="streamlit,chatgpt,openai,chapterify,shrithik,app,meta tags">
        <meta name="author" content="Shrithik Shahapure">
    </head>
    """,
    unsafe_allow_html=True
)

#Added Heading with HTML
st.markdown("<h1 style='text-align: center; color: white;'>Chapterify🐧</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: white;'>Generate Chapters and summaries for youtube videos </h5>", unsafe_allow_html=True)


st.write("<br><br>", unsafe_allow_html=True)
video_link = st.text_input('',placeholder="Please enter the link of your youtube video:")
st.write("<br>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)


col1, col2, col3, col4 = st.columns(4)

generate_chapters = col1.button('Generate Chapters')
generate_summary = col4.button('Generate Summary')

if generate_chapters:
    extract_chapters(video_link)

if generate_summary:
    extract_summary(video_link)

with col2:
    pass

with col3:
    pass


