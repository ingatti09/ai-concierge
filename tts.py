import pyttsx3

def parla(testo):
    engine = pyttsx3.init()   # 👈 importante: nuovo engine ogni volta
    engine.setProperty('rate', 175)

    print("\n🔊 Concierge:", testo)

    engine.say(testo)
    engine.runAndWait()

    engine.stop()