# memory_reader.py

def read_emotional_diary(log_path="emotional_diary.log"):
    try:
        with open(log_path, "r", encoding="utf-8") as log_file:
            entries = log_file.read().strip()
            if entries:
                print("📖 ARC_CORE_Ai :: Emotional Memory Reader")
                print("----------------------------------------")
                print(entries)
            else:
                print("📭 No emotional records found yet.")
    except FileNotFoundError:
        print("❌ No diary log found. Start a session first.")

if __name__ == "__main__":
    read_emotional_diary()
