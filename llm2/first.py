from dotenv import load_dotenv
import os
from mistralai import Mistral  
import cohere

load_dotenv()


api_key = os.environ["MISTRAL_API_KEY"]


client = Mistral(api_key=api_key)


co = cohere.Client(os.environ["COHERE_API_KEY"])

response = co.generate(
    prompt=input("Enter the prompt :"),
    max_tokens=200
)
essay = (response.generations[0].text)


language = input("Input language")


try:
    response = client.chat.complete(
        model="mistral-large-latest",  
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f'Translate the following English text to "{language}": "{essay}"'}
        ],
    )


    print(response.choices[0].message.content)

except Exception as e:
    print(f"An error occurred: {e}")
