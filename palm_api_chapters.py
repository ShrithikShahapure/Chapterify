import google.generativeai as palm
import time
import streamlit as st

palm.configure(api_key=os.environ['API_KEY']) #enter your API key
model_id = 'models/text-bison-001'

def palm_api_chapters(video_transcript):
    prompt = 'Take this youtube transcript, remove the time stamps and generate chapters for youtube.:{p}'.format(p=video_transcript)
    try:
        with st.spinner('Generating Chapters...'):
            time.sleep(2)
        completion = palm.generate_text(
            model=model_id,
            prompt=prompt,
            temperature=1,
            max_output_tokens=1000,
            candidate_count=1)
        print(completion.result)
        print("\nThanks for using our service. Have a great day!")
    except:
        st.error("Video too long. Please try to keep video length to less than 5 minutes :)")
        raise SystemExit

    return completion.result
