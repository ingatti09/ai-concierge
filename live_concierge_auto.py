import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from faster_whisper import WhisperModel
from concierge import rispondi
from tts import parla

fs = 16000
block_duration = 1  # 1 secondo per blocco
silence_threshold = 0.02
silence_limit = 3  # secondi di silenzio per fermarsi

print("Caricamento modello...")

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

print("Pronto. Parla quando vuoi...")

def is_silence(audio_chunk):
    return np.abs(audio_chunk).mean() < silence_threshold

while True:

    print("\n🎤 In ascolto... (parla)")

    recording = []
    silence_counter = 0

    while True:

        chunk = sd.rec(
            int(block_duration * fs),
            samplerate=fs,
            channels=1,
            dtype="float32"
        )

        sd.wait()

        recording.append(chunk)

        if is_silence(chunk):
            silence_counter += 1
        else:
            silence_counter = 0

        if silence_counter >= silence_limit:
            break

    audio = np.concatenate(recording, axis=0)

    write("audio.wav", fs, audio)

    print("🧠 Trascrizione...")

    segments, _ = model.transcribe("audio.wav")

    testo = ""

    for s in segments:
        testo += s.text

    print("\nCliente:", testo)

    risposta = rispondi(testo)

    parla(risposta)