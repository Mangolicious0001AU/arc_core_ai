# arc_core_launcher.py (CLI handler update)

import argparse
from test_emotion_chip import launch_emotional_terminal
from emotional_engine import export_memory_log_to_pdf
from growth_diary import growth_diary


def main():
    parser = argparse.ArgumentParser(description="ARC_CORE_Ai Launcher")
    parser.add_argument("--debug", action="store_true", help="Run in debug mode (no file writes)")
    parser.add_argument("--autochip", action="store_true", help="Skip menu and run emotion chip terminal directly")
    parser.add_argument("--export", action="store_true", help="Export memory log to PDF and exit")
    args = parser.parse_args()

    if args.export:
        export_memory_log_to_pdf()
        return

    if args.autochip:
        launch_emotional_terminal(debug=args.debug)
        return

    if args.debug:
        print("[DEBUG MODE ACTIVE]")

    while True:
        print("\n======== ARC_CORE_Ai Launcher ========")
        print("[1] Launch Emotional Terminal")
        print("[2] View Memory Log")
        print("[3] Export Memory to PDF")
        print("[4] Show Emotion Frequency Chart")
        print("[5] Exit")
        print("======================================")

        choice = input("\nChoose an option (1–5): ").strip()

        if choice == "1":
            launch_emotional_terminal(debug=args.debug)
        elif choice == "2":
            for log in growth_diary:
                print(f"- {log['timestamp']}: {log['input'][:60]}... [{log['mode']}]")
        elif choice == "3":
            export_memory_log_to_pdf()
        elif choice == "4":
            print("[TODO] Emotion Frequency Chart placeholder")
        elif choice == "5":
            print("Exiting ARC_CORE_Ai . . .")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
