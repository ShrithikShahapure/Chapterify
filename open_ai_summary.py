import openai
import os
import streamlit as st

openai.api_key = os.getenv("MY_SECRET_KEY")


def open_ai_summary(video_transcript):
    prompt = "Hello chatgpt"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role":"user","content":f"Based on the following youtube transcript, generate a summary of the video. Generate upto 200 words: {video_transcript}"}
            ]
        )
    except:
        st.error("Error in openAI")
        raise SystemExit



    content_value = response["choices"][0]["message"]["content"]

    return content_value



print("\nThanks for using our service. Have a great day!")