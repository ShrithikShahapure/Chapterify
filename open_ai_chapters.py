import openai

#openai part
# test = os.getenv("MY_SECRET_KEY")
# st.write(test)
openai.api_key = "ENTER-KEY"  #this is for temporary testing purposes
#os.getenv("MY_SECRET_KEY")



def open_ai_chapters(video_transcript):
    prompt = "Hello chatgpt"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role":"user","content":f"Based on the following youtube transcript, generate youtube chapters along with timestamps. Generate upto 6 timestamps: {video_transcript}"}
        ]
    )

    #print response
    content_value = response["choices"][0]["message"]["content"]
    return content_value


print("\nThanks for using our service. Have a great day!")
