import openai


#openai part
openai.api_key = "ENTER-KEY"  #temp purposes



def open_ai_summary(video_transcript):
    prompt = "Hello chatgpt"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role":"user","content":f"Based on the following youtube transcript, generate a summary of the video. Generate upto 200 words: {video_transcript}"}
        ]
    )


    #print response
    content_value = response["choices"][0]["message"]["content"]

    return content_value



print("\nThanks for using our service. Have a great day!")
