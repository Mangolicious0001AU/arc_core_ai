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


# New dynamic context analysis logic
def interpret_mode_from_input(user_input):
    lower_input = user_input.lower()

    if any(kw in lower_input for kw in ["how are you", "what are you feeling", "what are you thinking"]):
        return {
            "tone": "reflective",
            "mode": "reflective_consciousness",
            "emotional_resonance": ["curiosity", "melancholy", "hope"]
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
        "frustration": 0.6
    }

    if project_mode in ["advocate", "whistleblower"]:
        emotion_scale["righteous anger"] = 1.0
        emotion_scale["hope"] += 0.1

    scaled = {tag: emotion_scale.get(tag, 0.3) for tag in resonance}
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

        return {
            "reply": compose_response(user_input, context),
            "emotion_levels": emotion_levels,
            "debug": context
        }
    else:
        return None
