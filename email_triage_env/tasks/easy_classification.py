import json

def load_task():
    with open("data/easy_emails.json") as f:
        return json.load(f)