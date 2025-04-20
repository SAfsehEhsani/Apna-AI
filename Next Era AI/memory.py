import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_memory(q, a):
    memory = load_memory()
    memory.append((q, a))
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory[-5:], f)  # Keep last 5 messages
