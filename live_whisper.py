import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

fs = 16000
seconds = 5

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)


def trascrivi_audio():

    recording = sd.rec(
        int(seconds * fs),
        samplerate=fs,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write("audio.wav", fs, recording)

    segments, _ = model.transcribe("audio.wav")

    testo = "".join([s.text for s in segments])

    return testo