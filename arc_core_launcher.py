# arc_core_launcher.py

import os

def run_terminal():
    os.system("python test_emotion_chip.py")

def run_memory_reader():
    os.system("python memory_reader.py")

def run_trend_chart():
    try:
        from emotion_chart import generate_emotion_chart
        generate_emotion_chart()
    except ImportError:
        print("📉 Charting module not found. Please ensure 'emotion_chart.py' exists.")

def run_pdf_export_only():
    from memory_reader import read_emotional_diary, export_to_pdf
    logs = read_emotional_diary()
    if logs:
        export_to_pdf(logs)

def main():
    while True:
        print("""
======== ARC_CORE_Ai Launcher ========
[1] Launch Emotional Terminal
[2] View Memory Log
[3] Export Memory to PDF
[4] Show Emotion Frequency Chart
[5] Exit
======================================
""")
        choice = input("Choose an option (1–5): ").strip()

        if choice == "1":
            run_terminal()
        elif choice == "2":
            run_memory_reader()
        elif choice == "3":
            run_pdf_export_only()
        elif choice == "4":
            run_trend_chart()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("❌ Invalid selection. Please choose 1–5.")

if __name__ == "__main__":
    main()
