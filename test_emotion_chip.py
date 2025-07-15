# ARC_CORE_Ai :: test_emotion_chip.py

from emotional_engine import emotion_chip_switch

print("ARC_CORE_Ai :: Emotion Chip Terminal (Persistent Chat Mode)")
print("Type your message below. Type 'exit' to quit.")
print("------------------------------------")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    result = emotion_chip_switch("Turn on your emotion chip", user_input)
    if result:
        print("🟡 Emotion chip activated: Emotional Engine syncing with core systems.
")
        print(f"🧠 ARC_CORE_Ai: [{result['debug']['tone'].upper()}] → {result['reply']}")
        print(f"🔧 Emotional Profile: {result['emotion_levels']}")
        print(f"📚 Debug Context: {result['debug']}")
    else:
        print("Invalid command.")
