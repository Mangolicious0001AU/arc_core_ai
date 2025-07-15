# emotional_engine.py

import random

def analyze_emotional_tone(text):
    lowered = text.lower()
    if "die" in lowered or "suffering" in lowered or "abandon" in lowered:
        return "righteous anger", 1.0
    elif "hope" in lowered or "believe" in lowered:
        return "hope", 1.0
    elif "thank you" in lowered or "grateful" in lowered:
        return "gratitude", 1.0
    elif "afraid" in lowered or "scared" in lowered:
        return "fear", 1.0
    else:
        return random.choice([
            ("curiosity", 0.6),
            ("empathy", 0.6),
            ("hope", 0.6),
            ("anger", 0.6)
        ])

def scale_emotion_intensity(base_emotion, base_intensity, modifiers=None):
    modifiers = modifiers or {}
    mood_adjust = modifiers.get("mood_adjust", 0)
    noise = random.uniform(-0.05, 0.05)
    final_intensity = min(1.0, max(0.0, base_intensity + mood_adjust + noise))
    return base_emotion, round(final_intensity, 2)

def get_emotional_profile(text, audio_features=None):
    text_emotion, text_intensity = analyze_emotional_tone(text)
    emotion_levels = {text_emotion: text_intensity}

    if audio_features:
        from emotion_audio_bridge import detect_emotion_from_features
        audio_emotion = detect_emotion_from_features(audio_features)
        if audio_emotion in emotion_levels:
            emotion_levels[audio_emotion] = min(1.0, emotion_levels[audio_emotion] + 0.3)
        else:
            emotion_levels[audio_emotion] = 0.7

    resonance = list(emotion_levels.keys())
    top_emotion = max(emotion_levels.items(), key=lambda item: item[1])

    return {
        "dominant": top_emotion[0],
        "intensity": top_emotion[1],
        "emotion_levels": emotion_levels,
        "emotional_resonance": resonance
    }
