pip install SpeechRecognition pydub

import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Load the audio file
with sr.AudioFile("audio.wav") as source:
    print("Listening...")
    audio = recognizer.record(source)

try:
    # Recognize speech using Google's free API
    text = recognizer.recognize_google(audio)
    print("\n--- Transcription ---\n")
    print(text)

except sr.UnknownValueError:
    print("Could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results; {e}")
