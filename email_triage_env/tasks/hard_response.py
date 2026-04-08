import json

def load_task():
    with open("data/hard_emails.json") as f:
        return json.load(f)