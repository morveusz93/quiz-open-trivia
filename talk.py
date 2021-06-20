import pyttsx3 as tts


class Talk:
    def __init__(self, text):
        self.text = text
        engine = tts.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 125)
        engine.say(text)
        engine.runAndWait()
