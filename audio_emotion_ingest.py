# audio_emotion_ingest.py

import os
import librosa
import numpy as np

from emotional_engine import detect_emotion_from_features
from growth_diary import growth_diary, log_emotion_event

def extract_audio_features(file_path):
    try:
        y, sr = librosa.load(file_path)
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
        rms = np.mean(librosa.feature.rms(y=y))
        zero_crossing_rate = np.mean(librosa.feature.zero_crossing_rate(y))

        return {
            "tempo": tempo,
            "spectral_centroid": spectral_centroid,
            "rms": rms,
            "zero_crossing_rate": zero_crossing_rate
        }
    except Exception as e:
        print(f"Failed to process {file_path}: {e}")
        return None

def ingest_audio_file(file_path):
    features = extract_audio_features(file_path)
    if features:
        emotions = detect_emotion_from_features(features)
        log_emotion_event(file_path, emotions, mode="audio_reactive", tone="ambient")
        print(f"Logged emotional response to: {file_path}")
    else:
        print(f"Could not extract features for: {file_path}")

def batch_ingest_audio(directory_path):
    print(f"\n🎧 Ingesting audio files from: {directory_path}")
    for filename in os.listdir(directory_path):
        if filename.lower().endswith((".mp3", ".wav")):
            file_path = os.path.join(directory_path, filename)
            ingest_audio_file(file_path)

if __name__ == "__main__":
    target_dir = input("Enter path to audio directory: ")
    batch_ingest_audio(target_dir)
