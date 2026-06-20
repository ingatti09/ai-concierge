import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

fs = 16000
seconds = 5

print("Parla...")

recording = sd.rec(
    int(seconds * fs),
    samplerate=fs,
    channels=1
)

sd.wait()

write("audio.wav", fs, recording)

print("Sto elaborando...")

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

segments, info = model.transcribe("audio.wav")

print("\nLingua:", info.language)
print("\nTesto:")

for segment in segments:
    print(segment.text)