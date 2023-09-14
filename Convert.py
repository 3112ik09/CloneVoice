from vosk import Model, KaldiRecognizer
import pyaudio
import json
from googletrans import Translator
import wave
model = Model('./en')

recognizer = KaldiRecognizer(model, 16000)


# audio_file = wave.open("elon1min.wav", "rb")
# audio_data = audio_file.readframes(audio_file.getnframes())

# # Feed the audio data to the recognizer
# # rec.AcceptWaveform(audio_data)

# while True:
#     print("1")
#     data = audio_file.readframes(4000)
#     if len(data) == 0:
#         break
#     if rec.AcceptWaveform(data):
#         print(rec.Result())

# print(rec.FinalResult())

cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1,
                  rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
        resp = json.loads(recognizer.Result())
        listen_text = resp["text"]
        print(listen_text)
        # translator = Translator()
        # if listen_text != "":
        #     result = translator.translate(listen_text, src='hi', dest='en')
        #     print(result.text)

