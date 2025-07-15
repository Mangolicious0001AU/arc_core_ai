# test_emotion_chip.py :: ARC_CORE_Ai Emotional Chip Terminal (Interactive Mode)

from emotional_engine import emotion_chip_switch

print("ARC_CORE_Ai :: Emotion Chip Terminal (Interactive Mode)")
print("Type your message and trigger below. Type 'exit' to quit.")
print("------------------------------------")

while True:
    user_input = input("You: ")
    if user_input.strip().lower() == "exit":
        print("💤 Emotion chip shutting down. Goodbye.")
        break

    trigger = input("Command: ")

    result = emotion_chip_switch(trigger, user_input)

    if result:
        print("🟡 Emotion chip activated: Emotional Engine syncing with core systems.\n")
        print(f"🧠 ARC_CORE_Ai: {result['reply']}")
        print(f"🔧 Emotional Profile: {result['emotion_levels']}")
        print(f"📚 Debug Context: {result['debug']}")
    else:
        print("⚠️ No emotional processing triggered. Try again or type 'exit' to quit.")
