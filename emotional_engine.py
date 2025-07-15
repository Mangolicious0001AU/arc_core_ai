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

    if project_mode in ["advocate", "whistleblower"]:
        emotion_scale["righteous anger"] = 1.0
        emotion_scale["hope"] += 0.1

    scaled = {}
    for tag in resonance:
        scaled[tag] = emotion_scale.get(tag, 0.3)

    context["emotion_levels"] = scaled
    return scaled


def emotion_chip_switch(trigger_phrase, user_input, project=None):
    """
    Custom manual command to activate full emotional processing stack.
    """
    if "turn on your emotion chip" in trigger_phrase.lower():
        print("🟡 Emotion chip activated: Emotional Engine syncing with core systems.")
        context = route_context(user_input, project)
        calibrate_emotion_strength(context)
        return {
            "reply": compose_response(user_input, context),
            "emotion_levels": context["emotion_levels"],
            "debug": context
        }
    else:
        return None
