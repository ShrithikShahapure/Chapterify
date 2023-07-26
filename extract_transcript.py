import time
import os
import re
import streamlit as st
from convert_time import convert_time
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(video_link):

# this function extracts the video ID from a youtube link

    video_id_match = re.search(r"youtube\.com/watch\?v=([A-Za-z0-9_-]+)", video_link)
    if video_id_match:
        with st.spinner('Extracting VideoID ...'):
            time.sleep(2)
        return video_id_match.group(1)
    else:
        with st.spinner('Extracting VideoID ...'):
            time.sleep(2)
        st.error("Link Not Entered  Right, Try again.")
        raise SystemExit

def extract_transcript(video_link):

#retreive the transcript of the video using an api call

    video_id = extract_video_id(video_link)
    outls = []

    tx = YouTubeTranscriptApi.get_transcript(str(video_id),languages = ['en'])
    with st.spinner('Retrieving Transcript...'):
    	time.sleep(2)

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

        video_transcript = file.read()  # Read the contents of the file

    with st.spinner('Loading...'):
    	time.sleep(2)

    os.remove("op.txt")

    # st.write(video_transcript)
    return video_transcript

