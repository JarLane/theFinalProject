# Module.py
import wave
import numpy as np

def analyze_wav(file_path):
    with wave.open(file_path, 'rb') as wav_file:
        framerate = wav_file.getframerate()
        frames = wav_file.getnframes()
        duration = frames / float(framerate)

        signal = np.frombuffer(wav_file.readframes(frames), dtype=np.int16)
        frequencies = np.fft.fft(signal)
        frequencies = np.abs(frequencies)[:len(frequencies)//2]

    return duration, frequencies
