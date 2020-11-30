# tukoke2021
This code plays audio files one by one and waits for the user to choose a color for the recording.

## Dependencies
* `python3`
    * `tkinter`
    * `PIL`
    * `playsound`

All of the python libraries are available via `pip3` using the following command.
```
pip3 install tkinter pillow playsound
```

## Usage
To start the program, run `python main.py`. This opens up a window with a color picker. When you first click on the window, the first audio file is played. Then you are to click on a color that best fits the played audio clip. When you feel like done, just close the window normally; the recordings you have given a color are saved in the file `played` and the colors in the file `color.json`.

If you want to start over or the programs gives an error, you can run `python clear.py`. This will clear the played files and the recorded colors. The program asks you if you want to clear them. By entering `y`, all of the data is cleared irreversibly.
