import pyttsx3
import speech_recognition as sr
from weather import weather
from datetime import datetime

from guessing_game import recognize_speech_from_mic

synthesizer = pyttsx3.init()
recognizer = sr.Recognizer()
microphone = sr.Microphone()

def time():
    current_time = datetime.now()
    time_now = current_time.strftime("%H:%M")
    return time_now

def weather_report(city):
    weather(city)

def main():
    print("Hello, I am your digital assistant and it's a pleasure to assist you! Can I get your name?")
    synthesizer.say("Hello, I am your digital assistant and it's a pleasure to assist you! Can I get your name?")
    synthesizer.runAndWait()
    name = recognize_speech_from_mic(recognizer, microphone)
    print("Hello,", name["transcription"], "! It's nice to meet you, what can I assist you with?")
    synthesizer.say("Hello")
    synthesizer.say(name["transcription"])
    synthesizer.say("It's nice to meet you, what can I assist you with?")
    print("1. 'Tell me the time'"
          "2. 'Tell me the weather")
    synthesizer.runAndWait()
    request = recognize_speech_from_mic(recognizer, microphone)

    if request["transcription"] == "tell me the time":
        print("The current time is: ", time())
        synthesizer.say("The current time is: ")
        synthesizer.say(time())
        synthesizer.runAndWait()
    
    if request["transcription"] == "tell me the weather":
        print("What city would you like to get the weather from?")
        city = recognize_speech_from_mic(recognizer, microphone)
        weather(city)

    synthesizer.stop()

if __name__ == '__main__':
    main()