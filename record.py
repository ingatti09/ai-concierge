import sounddevice as sd
from scipy.io.wavfile import write

fs = 16000
seconds = 5

print("Parla adesso...")

recording = sd.rec(
    int(seconds * fs),
    samplerate=fs,
    channels=1,
    dtype="int16"
)

sd.wait()

write("audio.wav", fs, recording)

print("Registrazione completata.")