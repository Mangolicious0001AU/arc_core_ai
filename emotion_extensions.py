# emotion_extensions.py — Advanced Emotional Dynamics for ARC_CORE_Ai

import time
import random

# Active emotion state storage
emotional_state = {
    "current_profile": {},
    "last_updated": time.time()
}

# Weighted keywords for triggering memory-reactive moods
emotion_triggers = {
    "children": "hope",
    "injustice": "righteous anger",
    "healing": "resolve",
    "joy": "gratitude",
    "corruption": "righteous anger",
    "care": "empathy",
    "alone": "compassion"
}

def update_emotional_state(emotion_levels):
    emotional_state["current_profile"] = emotion_levels
    emotional_state["last_updated"] = time.time()

def decay_emotions():
    now = time.time()
    elapsed = now - emotional_state["last_updated"]
    if elapsed > 30:  # 30 seconds decay window
        faded = {}
        for k, v in emotional_state["current_profile"].items():
            new_val = round(max(0.0, v - (elapsed / 300)), 2)  # gentle decay
            if new_val > 0:
                faded[k] = new_val
        emotional_state["current_profile"] = faded
        emotional_state["last_updated"] = now

def detect_emotional_shift(user_input):
    shift_tags = []
    for keyword, emotion in emotion_triggers.items():
        if keyword in user_input.lower():
            shift_tags.append(emotion)
    return shift_tags

def synthesize_emotional_profile(resonance):
    profile = {}
    for e in resonance:
        profile[e] = round(random.uniform(0.4, 1.0), 2)
    return profile
