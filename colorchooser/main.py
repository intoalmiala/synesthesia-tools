import sys
import os
import json
from random import randrange

from playsound import playsound
import tkinter as tk
from PIL import Image, ImageTk


# Command line arguments
SIZE = tuple(map(int, sys.argv[1].split("x"))) if len(sys.argv) > 1 else (640, 640)


# I/O files
DIRECTORY = "assets/recordings"
OUTPUT_FILE = "colors.json"
COLOR_IMAGE = "assets/colorspace.png"


# Get files from directory
_, _, files = next(os.walk(DIRECTORY))


# Check for colors already done
if not os.path.exists(OUTPUT_FILE):
    with open(OUTPUT_FILE, "w") as f:
        json.dump({}, f, ensure_ascii=False)
        print(f"Created file '{OUTPUT_FILE}' for recording colors.")


# Load already done data
with open(OUTPUT_FILE) as f:
    colors = json.load(f)


# For keeping track of last recording and colors for it
lastindex = None
colorlist = []
lastevent = None

# Play random recording
def play(event):
    global lastindex, colorlist
    if not lastindex is None:
        colors[files[lastindex]] = colorlist
        colorlist = []
        files.pop(lastindex)
    if len(files):
        index = randrange(len(files))
        while files[index] in colors:
            files.pop(index)
            index = randrange(len(files))
        playsound(f"{DIRECTORY}/{files[index]}")
        lastindex = index
    else:
        print("All files played.")
    lastevent = "play"

# Get color from image on left click and play next recording
def getcolor(event):
    if not lastindex is None:
        value = img.getpixel((event.x, event.y))[:3]
        colorlist.append(value)
    lastevent = "getcolor"

# Write data and close window on exit
def onexit():
    with open("colors.json", "w") as f:
        json.dump(colors, f, ensure_ascii=False)
    root.destroy()


# Configure window
root = tk.Tk()
img = Image.open(COLOR_IMAGE).resize(SIZE)
img_tk = ImageTk.PhotoImage(img)
label = tk.Label(root, image = img_tk)
label.pack()
root.resizable(False, False)
root.bind("<Button 1>", getcolor)   # Left click
root.bind("<Button 3>", play)       # Right click
root.protocol("WM_DELETE_WINDOW", onexit)

root.mainloop()
