# ARC_CORE_Ai :: growth_diary.py

"""
Handles emotional memory logging for ARC_CORE_Ai.
Each interaction snapshot is stored in a chronological diary log
for export, review, or reinforcement learning.
"""

import json
import os
from datetime import datetime

DIARY_FILE = "emotion_memory_log.json"

def _load_log():
    if os.path.exists(DIARY_FILE):
        with open(DIARY_FILE, "r") as f:
            return json.load(f)
    return []

def _save_log(log):
    with open(DIARY_FILE, "w") as f:
        json.dump(log, f, indent=2)

growth_diary = []

# Load on import
_growth_cache = _load_log()
growth_diary.extend(_growth_cache)

def append(entry):
    timestamped = {
        "timestamp": datetime.now().isoformat(),
        **entry
    }
    growth_diary.append(timestamped)
    _save_log(growth_diary)

def export_summary():
    summary = {}
    for entry in growth_diary:
        for emotion, level in entry.get("emotions", {}).items():
            summary[emotion] = summary.get(emotion, 0) + level
    return summary

def get_latest(n=5):
    return growth_diary[-n:]
