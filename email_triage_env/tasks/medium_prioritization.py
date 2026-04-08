import json

def load_task():
    with open("data/medium_emails.json") as f:
        return json.load(f)