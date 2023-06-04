import re
import os
import openai
from youtube_transcript_api import YouTubeTranscriptApi
from convert_time import convert_time


#start here
print("Welcome to Chapterify. The one stop to Chapter Generation for Youtube ")
print('')
video_link = input("Please enter the link of your youtube video:")



#extract the video id of the video
def extract_video_id(video_link):
    video_id_match = re.search(r"youtube\.com/watch\?v=([A-Za-z0-9_-]+)", video_link)
    if video_id_match:
        return video_id_match.group(1)
    else:
        raise ValueError("Invalid YouTube URL")


video_id = extract_video_id(video_link)




#retreive the transcript of the video using an api call
outls = []
 
tx = YouTubeTranscriptApi.get_transcript(video_id,languages = ['en'])

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
    video = file.read()



    
    
#openai part
openai.api_key = "{ENTER YOUR API KEY HERE}"

prompt = "Hello chatgpt"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role":"user","content":f"Based on the following youtube transcript, generate youtube chapters along with timestamps. Generate upto 6 timestamps: {video}"}
    ]
)



#print response
content_value = response["choices"][0]["message"]["content"]
print(content_value)


print("\nThanks for using our service. Have a great day!")
