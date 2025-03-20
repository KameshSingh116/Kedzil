#Radhe Radhe 

import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")

def chat_with_gpt(prompt):
    client=openai.OpenAI()
    response=client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"system","content":"You are a helpful assistant."},
                  {"role":"user","content":prompt}]

 )
    return response['choices'][0]['message']['content']

print("Kedzil:Hello!, Type 'exit' to end the conversation.")

while True:
    user_input=input("You:")
    if user_input.lower()==exit:
        print("Kedzil:Radhe Radhe :)")
        break
    response=chat_with_gpt(user_input)
    print("Kedzil:",response)