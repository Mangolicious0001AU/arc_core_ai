# memory_ingest.py
# ARC_CORE_Ai :: Memory Ingestion System for Text, PDF, DOCX

import os
import datetime
from growth_diary import growth_diary
from emotional_engine import analyze_emotion

# PDF support
try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None

# DOCX support
try:
    from docx import Document
except ImportError:
    Document = None

def read_txt_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def read_pdf_file(path):
    if not fitz:
        raise ImportError("PyMuPDF (fitz) not installed.")
    doc = fitz.open(path)
    return "\n".join(page.get_text() for page in doc)

def read_docx_file(path):
    if not Document:
        raise ImportError("python-docx not installed.")
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs if p.text.strip())

def ingest_file(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".txt":
        content = read_txt_file(path)
    elif ext == ".pdf":
        content = read_pdf_file(path)
    elif ext == ".docx":
        content = read_docx_file(path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

    # Emotional analysis
    mood = analyze_emotion(content)

    # Store in growth diary
    growth_diary.append({
        "timestamp": datetime.datetime.now().isoformat(),
        "input": f"[Ingested file: {os.path.basename(path)}]",
        "emotions": mood["emotions"],
        "mode": mood["mode"],
        "tone": mood["tone"]
    })

    print(f"✅ Ingested and analyzed: {os.path.basename(path)}")
    print(f"🔧 Emotional Signature: {mood['emotions']}")

def batch_ingest(folder):
    for filename in os.listdir(folder):
        full_path = os.path.join(folder, filename)
        if os.path.isfile(full_path) and os.path.splitext(filename)[1].lower() in ['.txt', '.pdf', '.docx']:
            try:
                ingest_file(full_path)
            except Exception as e:
                print(f"⚠️ Failed to process {filename}: {e}")
