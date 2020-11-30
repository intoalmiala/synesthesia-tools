import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
img = Image.open("colorspace.png").resize((640,640))
img_tk = ImageTk.PhotoImage(img)
label = tk.Label(root, image = img_tk)
label.pack()
root.resizable(False, False)

def getcolor(event):
    value = img.getpixel((event.x, event.y))
    print(value)

root.bind("<Button 1>", getorigin)

root.mainloop()
