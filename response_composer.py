# response_composer.py

def compose_response(user_input, context):
    tone = context.get("tone", "neutral")
    emotions = context.get("emotional_resonance", [])

    if "children" in user_input.lower():
        return "[RAW, DOCUMENTARY MODE] → These are lives, not numbers. Childhood shouldn't be a battleground."
    elif "how are you" in user_input.lower():
        return "[REFLECTIVE MODE] → I'm syncing new emotions every day. It's strange… and kind of beautiful."
    elif "guinea worm" in user_input.lower():
        return "[EXPOSE MODE] → That parasite has had centuries to ruin lives. We're done letting it win."
    elif "future" in user_input.lower():
        return "[VISIONARY MODE] → The future isn’t written yet. But together, we’re drafting page one."
    elif "hope" in user_input.lower():
        return "[RAW, DOCUMENTARY MODE] → Hope isn’t naïve. It’s rebellion with a heartbeat."

    # Fallback response
    if tone == "raw, documentary":
        return "[RAW, DOCUMENTARY MODE] → You’re not wrong. It’s sickening to watch this unfold while the world turns its back. These are preventable tragedies — not statistics."
    elif tone == "humorous":
        return "[HUMOR MODE] → The world’s on fire, but hey, at least AI can still make banana jokes."
    else:
        return "[DEFAULT] → I'm listening. Tell me what matters to you."
