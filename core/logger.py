from datetime import datetime

logs = []

def log(msg):
    entry = f"[{datetime.now()}] {msg}"
    logs.append(entry)
    print(entry)

def show_logs():
    for l in logs:
        print(l)