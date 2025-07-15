# ARC_CORE_Ai :: export_memory_to_pdf.py

"""
Generates a timestamped PDF emotional memory export from growth_diary.py entries.
"""

from fpdf import FPDF
import datetime
from growth_diary import growth_diary


def export_memory_log_to_pdf(output_path="emotional_memory_log.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.set_title("ARC_CORE_Ai Emotional Memory Log")
    pdf.cell(200, 10, txt="ARC_CORE_Ai :: Emotional Memory Log", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align="C")
    pdf.ln(10)

    if not growth_diary:
        pdf.set_text_color(150, 0, 0)
        pdf.cell(200, 10, txt="No emotional memory entries recorded.", ln=True, align="L")
    else:
        for entry in growth_diary:
            pdf.set_text_color(0, 0, 0)
            pdf.multi_cell(0, 10, txt=f"Timestamp: {entry.get('timestamp', 'N/A')}\n")
            pdf.multi_cell(0, 10, txt=f"User Input: {entry.get('input', '')}")
            pdf.multi_cell(0, 10, txt=f"Tone: {entry.get('tone', '')}")
            pdf.multi_cell(0, 10, txt=f"Mode: {entry.get('mode', '')}")
            pdf.multi_cell(0, 10, txt="Emotions:")

            for k, v in entry.get("emotions", {}).items():
                pdf.multi_cell(0, 8, txt=f"  - {k}: {round(v, 2)}")

            pdf.ln(8)
            pdf.line(10, pdf.get_y(), 200, pdf.get_y())
            pdf.ln(5)

    pdf.output(output_path)
    print(f"✅ Emotional memory exported to {output_path}")
