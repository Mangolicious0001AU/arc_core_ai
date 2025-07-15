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
from emotion_extensions import (
    detect_emotional_shift,
    synthesize_emotional_profile,
    update_emotional_state,
    decay_emotions
)

def calibrate_emotion_strength(context, user_input):
    """
    Analyze context and user prompt to apply emotional intensity scores.
    Returns adjusted tone markers for use in response composer.
    """
    decay_emotions()
    resonance = context.get("emotional_resonance", [])
    project_mode = context.get("mode")

    # Real-time emotion triggers
    dynamic_tags = detect_emotional_shift(user_input)
    for tag in dynamic_tags:
        if tag not in resonance:
            resonance.append(tag)

    emotion_levels = synthesize_emotional_profile(resonance)

    # Boost if mission is urgent
    if project_mode in ["advocate", "whistleblower"]:
        if "righteous anger" in emotion_levels:
            emotion_levels["righteous anger"] = 1.0
        if "hope" in emotion_levels:
            emotion_levels["hope"] = min(emotion_levels["hope"] + 0.1, 1.0)

    update_emotional_state(emotion_levels)
    return emotion_levels

def emotion_chip_switch(trigger_phrase, user_input, project=None):
    """
    Custom manual command to activate full emotional processing stack.
    Trigger phrase: "Turn on your emotion chip"
    """
    context = route_context(user_input, project)
    emotion_levels = calibrate_emotion_strength(context, user_input)
    return {
        "reply": compose_response(user_input, context),
        "emotion_levels": emotion_levels,
        "debug": context
    }
