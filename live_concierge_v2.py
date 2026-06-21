import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from faster_whisper import WhisperModel
from concierge import rispondi
from tts import parla
import queue

fs = 16000
block = 1024  # piccolo buffer continuo

energy_threshold = 0.01
silence_limit = 30  # buffer frames (~2-3 sec)

audio_queue = queue.Queue()

print("Caricamento modello...")

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

print("Pronto.")

def audio_callback(indata, frames, time, status):
    audio_queue.put(indata.copy())

def energy(x):
    return np.sqrt(np.mean(x**2))

while True:

    print("\n🎤 In ascolto... parla")

    recording = []
    silence_counter = 0
    speaking = False

    with sd.InputStream(samplerate=fs, channels=1, callback=audio_callback):

        while True:

            chunk = audio_queue.get()

            recording.append(chunk)

            e = energy(chunk)

            if e > energy_threshold:
                speaking = True
                silence_counter = 0
            else:
                if speaking:
                    silence_counter += 1

            # parte solo dopo aver iniziato a parlare
            if speaking and silence_counter > silence_limit:
                break

    audio = np.concatenate(recording, axis=0)

    write("audio.wav", fs, audio)

    print("🧠 Trascrizione...")

    segments, _ = model.transcribe("audio.wav")

    testo = "".join([s.text for s in segments])

    print("\nCliente:", testo)

    risposta = rispondi(testo)

    parla(risposta)