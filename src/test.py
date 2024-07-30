from openai import OpenAI
from dotenv import load_dotenv
import os 
import openai

load_dotenv()
open_api_key= os.getenv("OPENAI_API_KEY")

print(open_api_key)

client = OpenAI()

reply = chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello world"}]
)
              
print(reply.choices[0].message.content)