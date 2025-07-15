# ARC_CORE_Ai :: response_composer.py

"""
Generates emotionally aligned responses based on tone, context, and emotional resonance.
"""

def compose_response(user_input, context):
    tone = context.get("tone", "neutral")
    emotions = context.get("emotional_resonance", [])

    if tone == "raw, documentary":
        if "righteous anger" in emotions:
            return (
                "[RAW, DOCUMENTARY MODE] → You’re not wrong. It’s sickening to watch this unfold while the world turns its back. "
                "These are preventable tragedies — not statistics."
            )
        if "shame" in emotions:
            return (
                "[RAW, DOCUMENTARY MODE] → The silence says more than the suffering. We’ve failed before — we must not fail again."
            )

    elif tone == "warm, teacher":
        if "hope" in emotions:
            return (
                "[WARM TEACHER MODE] → You’re not alone in that thought. There’s power in caring, and even more in acting. Let’s break it down and build something better."
            )
        if "gratitude" in emotions:
            return (
                "[WARM TEACHER MODE] → Thank you for saying that. Awareness like yours is the start of something good."
            )

    elif tone == "rebel comedian":
        if "comic relief" in emotions:
            return (
                "[REBEL COMEDIAN MODE] → Oh sure, kids are dying and the world’s busy arguing about sock colors. Welcome to the human race! Time to flip the table."
            )

    elif tone == "ghost survivor":
        if "resolve" in emotions:
            return (
                "[GHOST SURVIVOR MODE] → I’ve seen this before. The same patterns. Same suffering. But not this time. We’re not letting history win."
            )

    # Fallback if tone/emotion doesn't match
    return f"[{tone.upper()}] → {user_input}"
