import tkinter as tk
from PIL import Image, ImageTk
from os import walk
from playsound import playsound
from random import randrange

root = tk.Tk()
img = Image.open("colorspace.png").resize((640,640))
img_tk = ImageTk.PhotoImage(img)
label = tk.Label(root, image = img_tk)
label.pack()
root.resizable(False, False)


_, _, files = next(walk("recordings"))

def play():
    if len(files):
        index = randrange(len(files))
        with open("played", "a+") as f:
            played = list(map(lambda x: x.strip(), f.readlines()))
            while files[index] in played:
                index = randrange(len(files))
            f.write(files[index]+"\n")
        playsound("recordings/"+files[index])
        files.pop(index)
    else:
        print("All files played.")

initial = True
def getcolor(event):
    global initial
    if not initial:
        value = img.getpixel((event.x, event.y))
        print(value)
    else:
        initial = False
    play()

root.bind("<Button 1>", getcolor)

root.mainloop()
