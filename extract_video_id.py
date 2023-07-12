import time
import os
import re
import streamlit as st
from convert_time import convert_time
# from open_ai import open_ai
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(video_link):
    with st.spinner('extracting Video...'):
    	time.sleep(5)
    st.success('Done!')
    video_id_match = re.search(r"youtube\.com/watch\?v=([A-Za-z0-9_-]+)", video_link)
    if video_id_match:
        return video_id_match.group(1)
    else:
        st.write("Link Not Entered  Right, Try again.")

def extract_transcript(video_link):
    video_id = extract_video_id(video_link)


    #retreive the transcript of the video using an api call
    outls = []

    tx = YouTubeTranscriptApi.get_transcript(str(video_id),languages = ['en'])

    for i in tx:
        i['start'] = convert_time(i['start'])

    for i in tx:
        outtxt_1 = (i['text'])
        outtxt_2 = (i['start'])
        outtxt_3 = str(outtxt_2) +  ' ' + outtxt_1
        outls.append(outtxt_3)

        with open("op.txt", "a") as opf:
            opf.write(outtxt_3 + "\n")

    with open('op.txt', 'r') as file:
        # Read the contents of the file
        video_transcript = file.read()

    os.remove("op.txt")

    # Function to generate characters one by one
    # def generate_characters():
    #     for character in video_transcript:
    #         yield character
    #         time.sleep(0.1)  # Adjust the delay duration as needed
    #
    # # Create a generator object
    # char_generator = generate_characters()
    #
    # # Display the characters one by one
    # for character in char_generator:
    #     print(character, end='\r')
    #     st.text(character)



    # def hello(name):
    #     return 'Hello ' + name
    #     # video_link = st.text_input('Please enter the link of your youtube video:')
    #     first_variable = st.text_input("What's your name?")
    #     if first_variable:
    #         st.write(hello(first_variable))



    # output_placeholder = st.empty()
    # for character in video_transcript:
    #     textt = output_placeholder + character
    #     output_placeholder.text(textt)
    #     time.sleep(0.1)  # Adjust the delay duration as needed
    # hello(str('name'))
    st.write(video_transcript)
    return video_transcript

