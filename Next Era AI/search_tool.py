import os
import requests
from dotenv import load_dotenv
load_dotenv()

def search_web(query):
    headers = {"X-API-KEY": os.getenv("SERPER_API_KEY")}
    data = {"q": query}
    res = requests.post("https://google.serper.dev/search", json=data, headers=headers).json()
    
    if "organic" in res and len(res["organic"]) > 0:
        top = res["organic"][0]
        return f"🔍 {top['title']}\n{top['link']}\n\n{top['snippet']}"
    return "No search results found."
