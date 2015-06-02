import pyaudio

with Microphone() as source:    # open the microphone and start recording
    pass                        # do things here - `source` is the Microphone instance created above
                                # the microphone is automatically released at this point
