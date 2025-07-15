# ARC_CORE_Ai :: emotion_chart_viewer.py

import matplotlib.pyplot as plt
import json
import os

EMOTION_STATE_FILE = "emotion_states.json"

def show_emotion_frequency_chart():
    if not os.path.exists(EMOTION_STATE_FILE):
        print("No emotional data found to generate chart.")
        return

    with open(EMOTION_STATE_FILE, "r") as f:
        emotion_data = json.load(f)

    if not emotion_data:
        print("Emotion data is empty.")
        return

    emotions = list(emotion_data.keys())
    values = list(emotion_data.values())

    plt.figure(figsize=(10, 6))
    plt.barh(emotions, values)
    plt.xlabel("Emotion Strength")
    plt.title("ARC_CORE_Ai :: Emotional Frequency Chart")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    show_emotion_frequency_chart()
