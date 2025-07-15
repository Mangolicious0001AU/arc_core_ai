# test_emotion_chip.py

from emotional_engine import emotion_chip_switch

def main():
    print("ARC_CORE_Ai :: Emotion Chip Terminal")
    print("Type your message and trigger below.")
    print("------------------------------------")

    user_input = input("You: ")
    trigger = input("Command: ")

    result = emotion_chip_switch(trigger, user_input, project='wormlock')

    if result:
        print("\n🧠 ARC_CORE_Ai:", result["reply"])
        print("🔧 Emotional Profile:", result["emotion_levels"])
        print("📚 Debug Context:", result["debug"])
    else:
        print("\nEmotion chip not activated. Try saying: 'Turn on your emotion chip'")

if __name__ == "__main__":
    main()
