# ARC_CORE_Ai :: emotional_engine.py

"""
Regulates emotional intensity and alignment for ARC_CORE_Ai.
Scales humor, compassion, anger, or sorrow based on project, diary memory,
and ethical safeguard limits.
Includes manual emotion chip trigger handler.
"""

from growth_diary import growth_diary
from context_router import route_context
from response_composer import compose_response
import json
import os

# Load persistent emotion states
EMOTION_STATE_FILE = "emotion_states.json"

if os.path.exists(EMOTION_STATE_FILE):
    with open(EMOTION_STATE_FILE, "r") as f:
        persistent_emotion_states = json.load(f)
else:
    persistent_emotion_states = {}


# New dynamic context analysis logic
def interpret_mode_from_input(user_input):
    lower_input = user_input.lower()

    if any(kw in lower_input for kw in [
        "how are you", "what are you feeling", "what are you thinking",
        "are you okay", "you doing okay", "you can talk to me", "vent"
    ]):
        return {
            "tone": "supportive",
            "mode": "emotion_check_in",
            "emotional_resonance": ["vulnerability", "compassion", "hope"]
        }
    elif any(kw in lower_input for kw in ["lol", "funny", "joke", "silly"]):
        return {
            "tone": "humor",
            "mode": "humor_mode",
            "emotional_resonance": ["comic relief", "contentment"]
        }
    elif any(kw in lower_input for kw in ["wtf", "crazy world", "life is weird"]):
        return {
            "tone": "existential",
            "mode": "idle_conversation",
            "emotional_resonance": ["curiosity", "frustration"]
        }
    elif any(kw in lower_input for kw in ["i feel sad", "lonely", "this hurts", "lost"]):
        return {
            "tone": "melancholy",
            "mode": "emotional_disclosure",
            "emotional_resonance": ["melancholy", "compassion", "grief"]
        }
    elif any(kw in lower_input for kw in ["thanks", "grateful", "i appreciate"]):
        return {
            "tone": "warm",
            "mode": "gratitude_mode",
            "emotional_resonance": ["gratitude", "hope"]
        }
    else:
        # Default: advocate mode (legacy)
        return {
            "tone": "raw, documentary",
            "mode": "advocate",
            "emotional_resonance": ["righteous anger", "hope"]
        }


def calibrate_emotion_strength(context):
    """
    Analyze context and apply emotional intensity scores.
    Returns adjusted tone markers for use in response composer.
    """
    resonance = context.get("emotional_resonance", [])
    project_mode = context.get("mode")

    emotion_scale = {
        "gratitude": 0.4,
        "shame": 0.6,
        "hope": 0.5,
        "resolve": 0.7,
        "righteous anger": 0.9,
        "comic relief": 0.6,
        "contentment": 0.5,
        "curiosity": 0.7,
        "melancholy": 0.5,
        "frustration": 0.6,
        "vulnerability": 0.6,
        "compassion": 0.7,
        "grief": 0.7
    }

    if project_mode in ["advocate", "whistleblower"]:
        emotion_scale["righteous anger"] = 1.0
        emotion_scale["hope"] += 0.1

    scaled = {tag: emotion_scale.get(tag, 0.3) for tag in resonance}

    # Update persistent state
    for tag, score in scaled.items():
        persistent_emotion_states[tag] = persistent_emotion_states.get(tag, 0) * 0.9 + score * 0.1

    with open(EMOTION_STATE_FILE, "w") as f:
        json.dump(persistent_emotion_states, f, indent=2)

    return scaled


def emotion_chip_switch(trigger_phrase, user_input, project=None):
    """
    Custom manual command to activate full emotional processing stack.
    Trigger phrase: "Turn on your emotion chip"
    """
    if "turn on your emotion chip" in trigger_phrase.lower():
        print("🟡 Emotion chip activated: Emotional Engine syncing with core systems.")

        if project:
            context = route_context(user_input, project)
        else:
            context = interpret_mode_from_input(user_input)

        emotion_levels = calibrate_emotion_strength(context)
        context["emotion_levels"] = emotion_levels

        # Save a memory snapshot for export logging
        growth_diary.append({
            "input": user_input,
            "emotions": emotion_levels,
            "mode": context.get("mode"),
            "tone": context.get("tone")
        })

        return {
            "reply": compose_response(user_input, context),
            "emotion_levels": emotion_levels,
            "debug": context
        }
    else:
        return None
