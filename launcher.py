# launcher.py

import os
from test_emotion_chip import launch_emotion_terminal
from view_memory_log import view_log
from export_memory_to_pdf import export_memory
from emotion_chart_viewer import show_chart
from emotional_test_bench import run_emotional_test_bench

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear_screen()
        print("Starting ARC_CORE_Ai Main Menu...\n")
        print("======== ARC_CORE_Ai Launcher ========")
        print("[1] Launch Emotional Terminal")
        print("[2] View Memory Log")
        print("[3] Export Memory to PDF")
        print("[4] Show Emotion Frequency Chart")
        print("[5] Exit")
        print("[6] Emotional Test Bench")
        print("======================================\n")

        choice = input("Choose an option (1–6): ").strip()

        if choice == '1':
            launch_emotion_terminal()
        elif choice == '2':
            view_log()
        elif choice == '3':
            export_memory()
        elif choice == '4':
            show_chart()
        elif choice == '5':
            print("Exiting ARC_CORE_Ai...")
            break
        elif choice == '6':
            run_emotional_test_bench()
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()
