# This program uses code from: https://python-sounddevice.readthedocs.io/en/0.4.1/examples.html#recording-with-arbitrary-duration

import sys

import sounddevice as sd
import soundfile as sf
from playsound import playsound
import numpy
import tkinter as tk


# Command line arguments
INPUT_FILE = sys.argv[1] if len(sys.argv) > 1 else "words"
OUTPUT_DIRECTORY = sys.argv[2] if len(sys.argv) > 2 else "recordings"


# Get words to record
with open(INPUT_FILE) as f:
    words = list(map(lambda x: x.strip(), f.readlines()))


# Audio numbers
SAMPLERATE = 44100
CHANNELS = 1
BLOCKSIZE = 512


word_index = 0
word_text = words[0]
filepath = f"{OUTPUT_DIRECTORY}/{word_text}.wav"

recording = False
stream = None
soundfile = None


# Functions for recording and playing audio
def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    soundfile.write(indata.copy())

def start_recording():
    global recording, stream, soundfile
    if not recording:
        recording = True
        stream = sd.InputStream(samplerate=SAMPLERATE, blocksize=BLOCKSIZE, channels=CHANNELS, callback=callback)
        soundfile = sf.SoundFile(filepath, "w", SAMPLERATE, CHANNELS)
        stream.start()

def stop_recording():
    global recording
    if recording:
        recording = False
        stream.stop()
        stream.close()
        soundfile.close()

def play():
    playsound(filepath)


# Function for getting next word
def next_word():
    global word_index, word_text, filepath
    word_index += 1
    if word_index == len(words):
        word_label.config(text="ALL WORDS RECORDED")
        record_button.pack_forget()
        stop_button.pack_forget()
        play_button.pack_forget()
    elif word_index > len(words):
        root.destroy()
    else:
        word_text = words[word_index]
        filepath = f"{OUTPUT_DIRECTORY}/{word_text}.wav"
        word_label.config(text=word_text)


# Configure window
root = tk.Tk()

word_label = tk.Label(root, text=word_text)
record_button = tk.Button(text="start", command=start_recording)
stop_button = tk.Button(text="stop", command=stop_recording)
play_button = tk.Button(text="play", command=play)
next_button = tk.Button(text="next", command=next_word)

word_label.pack()
record_button.pack()
stop_button.pack()
play_button.pack()
next_button.pack()

root.mainloop()

