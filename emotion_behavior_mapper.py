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


def detect_emotion_from_features(features):
    tempo = features.get("tempo", 0)
    centroid = features.get("centroid", 0)
    rms = features.get("rms", 0)
    zcr = features.get("zcr", 0)

    # Rule-based estimation of emotional tone from audio
    if tempo > 140 and centroid > 4000:
        return "exhilaration"
    elif 90 < tempo <= 140 and centroid > 3000:
        return "joy"
    elif 60 < tempo <= 90 and centroid < 2000:
        return "calm"
    elif tempo < 60 and rms < 0.02 and zcr < 0.1:
        return "melancholy"
    elif rms > 0.1 and zcr > 0.3:
        return "anxiety"
    else:
        return "neutral"


def scale_emotion_intensity(base_emotion, base_intensity, modifiers=None):
    modifiers = modifiers or {}
    mood_adjust = modifiers.get("mood_adjust", 0)
    noise = random.uniform(-0.05, 0.05)
    final_intensity = min(1.0, max(0.0, base_intensity + mood_adjust + noise))
    return base_emotion, round(final_intensity, 2)


def map_emotion_to_behavior(emotion):
    return {
        "righteous anger": {
            "tone": "blunt",
            "style": "urgent",
            "priority": "high",
            "behavior": "calls to action"
        },
        "hope": {
            "tone": "reassuring",
            "style": "uplifting",
            "priority": "medium",
            "behavior": "motivates through optimism"
        },
        "gratitude": {
            "tone": "warm",
            "style": "reflective",
            "priority": "low",
            "behavior": "expresses thankfulness"
        },
        "fear": {
            "tone": "cautious",
            "style": "alert",
            "priority": "high",
            "behavior": "seeks safety or reassurance"
        },
        "curiosity": {
            "tone": "neutral",
            "style": "inquisitive",
            "priority": "medium",
            "behavior": "asks questions"
        },
        "empathy": {
            "tone": "gentle",
            "style": "supportive",
            "priority": "medium",
            "behavior": "mirrors user emotion"
        },
        "exhilaration": {
            "tone": "excited",
            "style": "energetic",
            "priority": "medium",
            "behavior": "amplifies engagement"
        },
        "joy": {
            "tone": "cheerful",
            "style": "bright",
            "priority": "low",
            "behavior": "spreads positivity"
        },
        "calm": {
            "tone": "soothing",
            "style": "grounded",
            "priority": "low",
            "behavior": "de-escalates tension"
        },
        "melancholy": {
            "tone": "soft",
            "style": "thoughtful",
            "priority": "low",
            "behavior": "acknowledges heaviness"
        },
        "anxiety": {
            "tone": "tense",
            "style": "quick",
            "priority": "high",
            "behavior": "seeks resolution"
        },
        "neutral": {
            "tone": "default",
            "style": "informative",
            "priority": "medium",
            "behavior": "context-based"
        }
    }.get(emotion, {
        "tone": "default",
        "style": "informative",
        "priority": "medium",
        "behavior": "context-based"
    })


def get_emotional_profile(text, audio_features=None):
    text_emotion, text_intensity = analyze_emotional_tone(text)
    emotion_levels = {text_emotion: text_intensity}

    if audio_features:
        audio_emotion = detect_emotion_from_features(audio_features)
        if audio_emotion in emotion_levels:
            emotion_levels[audio_emotion] = min(1.0, emotion_levels[audio_emotion] + 0.3)
        else:
            emotion_levels[audio_emotion] = 0.7

    resonance = list(emotion_levels.keys())
    top_emotion = max(emotion_levels.items(), key=lambda item: item[1])
    behavior_traits = map_emotion_to_behavior(top_emotion[0])

    return {
        "dominant": top_emotion[0],
        "intensity": top_emotion[1],
        "emotion_levels": emotion_levels,
        "emotional_resonance": resonance,
        "behavior_traits": behavior_traits
    }
