import openai

#openai part
openai.api_key = "{ENTER YOUR API KEY HERE}"

prompt = "Hello chatgpt"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role":"user","content":f"Based on the following youtube transcript, generate youtube chapters along with timestamps. Generate upto 6 timestamps: {video}"}
    ]
)


response1 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role":"user","content":f"Based on the following youtube transcript, generate youtube chapters along with timestamps. Generate upto 6 timestamps: {video}"}
    ]
)


#print response
content_value = response["choices"][0]["message"]["content"]
print(content_value)


print("\nThanks for using our service. Have a great day!")