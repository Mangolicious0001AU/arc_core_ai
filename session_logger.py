# session_logger.py

from datetime import datetime

def log_emotional_session(user_input, reply, context):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"""\n=== {timestamp} ===
You: {user_input}
ARC_CORE_Ai: {reply}
Emotional Profile: {context.get('emotion_levels')}
Debug Context: {context.get('debug')}
----------------------------\n"""
    with open("emotional_diary.log", "a", encoding="utf-8") as diary:
        diary.write(log_entry)
