# test_emotion_chip.py — Cleaned Emotional Terminal (v2.1)

from emotional_engine import emotion_chip_switch
import datetime

def log_emotion(entry, response, levels, context):
    with open("emotional_diary.log", "a", encoding="utf-8") as log:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] USER: {entry}\n")
        log.write(f"AI: {response}\n")
        log.write(f"Emotional Profile: {levels}\n")
        log.write(f"Debug Context: {context}\n")
        log.write("----------------------------\n")

print("ARC_CORE_Ai :: Emotion Chip Terminal (Persistent Chat Mode)")
print("Type your message below. Type 'exit' to quit.")
print("------------------------------------")

emotion_chip_on = False

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        break

    if not emotion_chip_on:
        print("🟡 Emotion chip activated: Emotional Engine syncing with core systems.")
        emotion_chip_on = True

    # Don't repeat activation messages inside switch
    result = emotion_chip_switch("", user_input)  # Empty string skips internal "trigger" print
    if result:
        print(f"\n🧠 ARC_CORE_Ai: {result['reply']}")
        print(f"🔧 Emotional Profile: {result['emotion_levels']}")
        print(f"📚 Debug Context: {result['debug']}")
        log_emotion(user_input, result['reply'], result['emotion_levels'], result['debug'])
    else:
        print("⚠️ Failed to process emotional input.")
