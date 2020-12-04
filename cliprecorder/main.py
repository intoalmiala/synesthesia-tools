# This program uses code from: https://python-sounddevice.readthedocs.io/en/0.4.1/examples.html#recording-with-arbitrary-duration

import queue
import sys

import sounddevice as sd
import soundfile as sf
import numpy
import tkinter as tk


# Command line arguments
INPUT_FILE = sys.argv[1] if len(sys.argv) > 1 else "words"
OUTPUT_DIRECTORY = sys.argv[2] if len(sys.argv) > 2 else "recordings"


# Get words to record
with open(INPUT_FILE) as f:
    words = list(map(lambda x: x.strip(), f.readlines()))


# Initialize queue for audio recording
q = queue.Queue()


# Audio numbers
SAMPLERATE = 44100
CHANNELS = 1


recording = False
stream = None


# Function for audio processing
def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())


# Function for recording audio
def record():
    global recording, stream
    if not recording:
        recording = True
        stream = sd.InputStream(samplerate=SAMPLERATE, channels=CHANNELS, callback=callback)
        stream.start()

def stop():
    global recording, stream
    if recording:
        recording = False
        stream.stop()
        stream.close()
        with sf.SoundFile("test.wav", "w", SAMPLERATE, CHANNELS) as f:
            while not q.empty():
                f.write(q.get())



# Configure window
root = tk.Tk()
play = tk.Button(text="start", command=record)
stop = tk.Button(text="stop", command=stop)
play.pack()
stop.pack()
root.mainloop()


for word in words:
    filename = f"{OUTPUT_DIRECTORY}/{word}.wav"



