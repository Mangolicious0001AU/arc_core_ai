# memory_reader.py

from datetime import datetime
from fpdf import FPDF

def read_emotional_diary(log_path="emotional_diary.log", filter_term=None):
    try:
        with open(log_path, "r", encoding="utf-8") as log_file:
            entries = log_file.read().strip().split("\n----------------------------\n")
            if not entries or entries == ['']:
                print("📭 No emotional records found yet.")
                return []

            if filter_term:
                entries = [e for e in entries if filter_term in e]

            print("📖 ARC_CORE_Ai :: Emotional Memory Reader")
            print("----------------------------------------")
            for e in entries:
                print(e.strip())
                print("----------------------------")
            return entries
    except FileNotFoundError:
        print("❌ No diary log found. Start a session first.")
        return []

def export_to_pdf(entries, filename="emotional_diary_export.pdf"):
    if not entries:
        print("⚠️ No entries to export.")
        return

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for entry in entries:
        for line in entry.strip().splitlines():
            pdf.multi_cell(0, 10, line)
        pdf.ln(5)

    pdf.output(filename)
    print(f"✅ Exported to {filename}")

if __name__ == "__main__":
    print("Enter a date or keyword to filter (or press Enter to skip):")
    term = input("Filter: ").strip()
    logs = read_emotional_diary(filter_term=term if term else None)

    if logs:
        save = input("Export to PDF? (y/n): ").strip().lower()
        if save == "y":
            export_to_pdf(logs)
