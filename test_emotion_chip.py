# test_emotion_chip.py :: ARC_CORE_Ai Emotional Chip Terminal (Persistent Mode)

from emotional_engine import emotion_chip_switch

print("ARC_CORE_Ai :: Emotion Chip Terminal (Persistent Chip Mode)")
print("Type your message below. Type 'exit' to quit.")
print("------------------------------------")

# Initial activation of the emotion chip
trigger_phrase = "Turn on your emotion chip"
first_input = input("You: ")
chip_state = emotion_chip_switch(trigger_phrase, first_input)

if chip_state:
    print("🟡 Emotion chip activated: Emotional Engine syncing with core systems.\n")
    print(f"🧠 ARC_CORE_Ai: {chip_state['reply']}")
    print(f"🔧 Emotional Profile: {chip_state['emotion_levels']}")
    print(f"📚 Debug Context: {chip_state['debug']}")
else:
    print("⚠️ Failed to activate emotion chip.")
    exit()

# Enter persistent emotional interaction mode
while True:
    user_input = input("You: ")
    if user_input.strip().lower() == "exit":
        print("💤 Emotion chip shutting down. Goodbye.")
        break

    result = emotion_chip_switch(trigger_phrase, user_input)

    if result:
        print(f"🧠 ARC_CORE_Ai: {result['reply']}")
        print(f"🔧 Emotional Profile: {result['emotion_levels']}")
        print(f"📚 Debug Context: {result['debug']}")
    else:
        print("⚠️ Emotional processing error. Try again or type 'exit' to quit.")
