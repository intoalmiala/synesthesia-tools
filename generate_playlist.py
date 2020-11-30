from os import walk

_, _, files = next(walk("recordings"))

with open("playlist", "w") as playlist:
    for file in files:
        playlist.write(file+"\n")
