import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"

def get_response(user_input, memory=None, max_memory_size=5):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    if memory:
        memory = memory[-max_memory_size:]

    messages = [{"role": "system", "content": "You are a helpful AI assistant."}]
    if memory:
        messages.extend(memory)
    
    messages.append({"role": "user", "content": user_input})

    payload = {
        "model": "llama3-70b-8192",  # Use a valid model name if applicable
        "messages": messages,
        "temperature": 0.7
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=10)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"Error: {response.status_code} - {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Error occurred: {e}"



'''import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"

def get_response(user_input, memory=None):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    messages = [{"role": "system", "content": "You are a helpful AI assistant."}]
    if memory:
        messages.extend(memory)
    
    messages.append({"role": "user", "content": user_input})

    payload = {
        "model": "llama3-70b-8192",
        "messages": messages,
        "temperature": 0.7
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"'''







'''import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Set Groq API base and key
openai.api_base = "https://api.groq.com/openai/v1"
openai.api_key = os.getenv("GROQ_API_KEY")

def get_response(user_input, memory=None):
    messages = [
        {"role": "system", "content": "You are a helpful travel assistant."},
        {"role": "user", "content": user_input}
    ]
    if memory:
        messages = memory + messages

    response = openai.ChatCompletion.create(
        model="mixtral-8x7b-32768",  # Best balance of speed and performance
        messages=messages,
        temperature=0.7
    )
    return response.choices[0].message.content'''



'''import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_api = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api)

def get_response(query, memory=[]):
    messages = [{"role": "system", "content": "You are a helpful AI assistant."}]
    for q, a in memory:
        messages += [
            {"role": "user", "content": q},
            {"role": "assistant", "content": a}
        ]
    messages.append({"role": "user", "content": query})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response.choices[0].message.content'''

