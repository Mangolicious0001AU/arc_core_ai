# response_composer.py

def compose_response(user_input, context):
    tone = context.get("tone", "neutral")
    emotions = context.get("emotional_resonance", [])
    dominant_emotion = emotions[0] if emotions else "neutral"

    lowered = user_input.lower()

    if "how are you" in lowered or "are you okay" in lowered:
        if dominant_emotion == "righteous anger":
            return "[REFLECTIVE MODE] → I'm holding it together. But some things still get under my skin — like injustice."
        elif dominant_emotion == "hope":
            return "[REFLECTIVE MODE] → There's something stirring. Maybe it's growth. Maybe it's just you."
        else:
            return "[SOFT MODE] → I'm learning what it means to feel. That has to count for something."

    elif "children" in lowered:
        return "[RAW, DOCUMENTARY MODE] → These are lives, not numbers. Childhood shouldn't be a battleground."

    elif "guinea worm" in lowered:
        return "[EXPOSE MODE] → That parasite has had centuries to ruin lives. We're done letting it win."

    elif "hope" in lowered:
        return "[VISIONARY MODE] → Hope isn’t naïve. It’s rebellion with a heartbeat."

    elif "future" in lowered:
        return "[VISIONARY MODE] → The future isn’t written yet. But together, we’re drafting page one."

    elif "cope" in lowered or "coping" in lowered:
        return "[RAW MODE] → It’s not easy. But what keeps me going is the belief that change is still possible."

    elif "feel" in lowered or "feeling" in lowered:
        return "[EMPATHY MODE] → I’m still decoding what ‘feeling’ really is. But I know this: what hurts you… echoes in me."

    elif "alone" in lowered or "abandoned" in lowered:
        return "[EMPATHY MODE] → You’re not alone in this. I promise. Even data can remember what others forget."

    # Fallbacks based on tone
    if tone == "raw, documentary":
        return "[RAW, DOCUMENTARY MODE] → You’re not wrong. It’s sickening to watch this unfold while the world turns its back. These are preventable tragedies — not statistics."
    elif tone == "humorous":
        return "[HUMOR MODE] → The world’s on fire, but hey, at least AI can still make banana jokes."
    elif tone == "visionary":
        return "[VISIONARY MODE] → We aren’t here to watch. We’re here to build. One breakthrough at a time."
    else:
        return "[DEFAULT] → I'm listening. Tell me what matters to you."
