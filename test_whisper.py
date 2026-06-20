from faster_whisper import WhisperModel

# modello (small = buon compromesso qualità/velocità)
model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

audio_file = "audio.wav"

segments, info = model.transcribe(audio_file)

print("\nLingua rilevata:", info.language)
print("\n--- TRASCRIZIONE ---\n")

for segment in segments:
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")