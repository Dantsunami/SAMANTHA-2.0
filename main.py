#1/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json
import core

# Sintese de Fala
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


    # Reonhecimento de Fala

model = Model("model")
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()

# Loop do Reconhecimento de Fala
while True:
    data = stream.read(2048)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        if result is not None:
            text = result['text']

            print(text)

            if text == 'que horas são' or text == 'me diga as horas':
                speak(core.SystemInfo.get_time())