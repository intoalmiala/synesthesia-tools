import os
import json
from playsound import playsound
from random import randrange
import tkinter as tk
from PIL import Image, ImageTk

DIRECTORY = "recordings"
_, _, files = next(os.walk(DIRECTORY))

if not os.path.exists("played"):
    with open("played", "w") as f:
        print("Created file 'played' for tracking played files.")
if not os.path.exists("colors.json"):
    with open("colors.json", "w") as f:
        print("Created file 'colors.json' for recording colors.")

with open("played") as f:
    played = list(map(lambda x: x.strip(), f.readlines()))
with open("colors.json") as f:
    colors = json.load(f)

lastindex = None

def play():
    global lastindex
    if len(files):
        index = randrange(len(files))
        while files[index] in played:
            index = randrange(len(files))
        playsound(f"{DIRECTORY}/{files[index]}")
        lastindex = index
    else:
        print("All files played.")

def getcolor(event):
    #global played, colors
    if not lastindex is None:
        value = img.getpixel((event.x, event.y))[:3]
        played.append(files[lastindex]+"\n")
        colors[files[lastindex]] = value
        files.pop(lastindex)
    play()

def onexit():
    with open("played", "w") as f:
        f.writelines(played)
    with open("colors.json", "w") as f:
        json.dump(colors, f)
    root.destroy()

root = tk.Tk()
img = Image.open("colorspace.png").resize((640,640))
img_tk = ImageTk.PhotoImage(img)
label = tk.Label(root, image = img_tk)
label.pack()
root.resizable(False, False)
root.bind("<Button 1>", getcolor)
root.protocol("WM_DELETE_WINDOW", onexit)

root.mainloop()
