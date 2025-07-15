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
        "comic relief": 0.6
    }

    # Boost for mission urgency
    if project_mode in ["advocate", "whistleblower"]:
        emotion_scale["righteous anger"] = 1.0
        emotion_scale["hope"] += 0.1

    # Filter and return scaled output
    scaled = {}
    for tag in resonance:
        scaled[tag] = emotion_scale.get(tag, 0.3)  # Default gentle weight

    return scaled


def emotion_chip_switch(trigger_phrase, user_input, project=None):
    """
    Custom manual command to activate full emotional processing stack.
    Trigger phrase: "Turn on your emotion chip"
    """
    if "turn on your emotion chip" in trigger_phrase.lower():
        print("🟡 Emotion chip activated: Emotional Engine syncing with core systems.")
        context = route_context(user_input, project)
        emotion_levels = calibrate_emotion_strength(context)
        return {
            "reply": compose_response(user_input, context),
            "emotion_levels": emotion_levels,
            "debug": context
        }
    else:
        return None


# This system prevents emotional extremes without ethical grounding.
# Emotion chip trigger now available for manual ignition.
