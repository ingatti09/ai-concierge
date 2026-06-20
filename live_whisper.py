import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

print("Caricamento modello...")

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

print("Pronto.")

fs = 16000

while True:

    input("\nPremi INVIO per parlare (CTRL+C per uscire)")

    print("Registrazione...")

    recording = sd.rec(
        int(5 * fs),
        samplerate=fs,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write("audio.wav", fs, recording)

    print("Trascrizione...")

    segments, info = model.transcribe("audio.wav")

    print("\nHai detto:")

    for segment in segments:
        print(segment.text)