#dummy change 2
                                               # NOTE: this requires PyAudio because it uses the Microphone class

#only works from command line. not from IDLE

import speech_recognition as sr
#from os import syste # for osx TTS
import subprocess

print("1")
r = sr.Recognizer(language = "ja")
with sr.Microphone() as source:                # use the default microphone as the audio source
    audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
print("2")
try:

    print("You said " + r.recognize(audio))    # recognize speech using Google Speech Recognition
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")
