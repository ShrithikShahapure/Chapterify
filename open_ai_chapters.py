import openai
import os
import streamlit as st


openai.api_key = os.getenv("MY_SECRET_KEY")



def open_ai_chapters(video_transcript):
    prompt = "Hello chatgpt"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role":"user","content":f"Based on the following youtube transcript, generate youtube chapters along with timestamps. Generate upto 6 timestamps: {video_transcript}"}
            ]
        )
    except:
        st.error("Error in openAI")
        raise SystemExit

    #print response
    content_value = response["choices"][0]["message"]["content"]
    return content_value


print("\nThanks for using our service. Have a great day!")


