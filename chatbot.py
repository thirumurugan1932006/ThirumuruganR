import json
from datetime import datetime
from database import get_connection

def load_stories():
    with open("stories.json", encoding="utf-8") as f:
        return json.load(f)

def find_story(query):
    stories = load_stories()
    for story in stories:
        if query in story["title"] or query in story["content"]:
            return story["content"]
    return "மன்னிக்கவும், இந்தக் கதையை நான் காணவில்லை."

def save_history(user_id, question, answer):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history (user_id, question, answer, created_at) VALUES (?, ?, ?, ?)",
                   (user_id, question, answer, datetime.now()))
    conn.commit()
    conn.close()
  
