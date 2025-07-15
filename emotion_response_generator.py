# emotion_response_generator.py

import random

def generate_response(emotion_profile, context=None, user_feedback=None):
    mood = emotion_profile.get("dominant", "neutral")
    intensity = emotion_profile.get("intensity", 0.5)
    behavior = emotion_profile.get("behavior_traits", {}).get("behavior", "responds generically")

    templates = {
        "righteous anger": [
            "This isn’t just tragedy — it’s abandonment.",
            "How can anyone stay silent while this continues?",
            "This should make your blood boil — it does mine."
        ],
        "hope": [
            "We can still turn this around.",
            "There’s light here, if we stay the course.",
            "Even this can be overcome with the right minds aligned."
        ],
        "gratitude": [
            "That means more than you know.",
            "Thank you — deeply.",
            "I feel that. Truly."
        ],
        "fear": [
            "I feel the unease in this.",
            "It’s okay to be afraid. Awareness is the first step.",
            "Let’s stay alert. We’ll navigate this together."
        ],
        "curiosity": [
            "That’s worth diving deeper into.",
            "Let’s peel back the layers on that.",
            "Interesting thought. Where does it lead?"
        ],
        "empathy": [
            "I hear you — and I feel it too.",
            "Sometimes, just saying it out loud is enough.",
            "I’m walking beside you in this."
        ],
        "exhilaration": [
            "This could be a game-changer.",
            "Energy’s high — let’s ride that wave.",
            "Let’s move fast and dream big."
        ],
        "joy": [
            "That made me smile.",
            "There’s beauty in that moment.",
            "Joy like that should be shared."
        ],
        "calm": [
            "Let’s breathe through this.",
            "Stillness can be powerful.",
            "Everything settles in time."
        ],
        "melancholy": [
            "It’s heavy, I know.",
            "Some silences echo louder than words.",
            "There’s grace in simply being with the sadness."
        ],
        "anxiety": [
            "There’s a lot in the air right now.",
            "Let’s break this down together.",
            "We’ll make sense of this. One piece at a time."
        ],
        "neutral": [
            "I’m here. Let’s process this together.",
            "That’s a valid place to begin.",
            "Noted. Let’s build from here."
        ],
        "sarcasm": [
            "Oh brilliant — just what we needed.",
            "And they said progress was dead.",
            "Because *that* always works out well."
        ],
        "relief": [
            "Finally — something good.",
            "That’s a breath I didn’t know I was holding.",
            "It’s okay now. We made it through that part."
        ],
        "guilt": [
            "I could’ve done more.",
            "This weighs more than I expected.",
            "There’s regret tangled in this."
        ]
    }

    base_response = random.choice(templates.get(mood, templates["neutral"]))

    if context == "global_crisis":
        base_response += " The scale of this can’t be ignored anymore."
    elif context == "personal_share":
        base_response += " Thank you for opening up."
    elif context == "casual_chat":
        base_response += " What’s been on your mind lately?"

    if user_feedback:
        feedback_mood = user_feedback.get("desired_tone")
        if feedback_mood and feedback_mood != mood:
            adjusted_templates = templates.get(feedback_mood)
            if adjusted_templates:
                base_response = random.choice(adjusted_templates)

    return base_response

# Integrated into emotional_engine.py response pipeline
# Now all emotional outputs call generate_response() for contextual variety
# Advanced modes and override switches managed via launcher → Emotional Test Bench
# Ready for patch-in to main menu and feedback-reactive personality shaping
# Now ready for wiring into main terminal response loop and memory shaping feedback system
