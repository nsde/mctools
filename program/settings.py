import main

import os
import tkinter as tk

winTitle = "Styx MCTools"

fileDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.dirname(fileDir)

fgColor = "white"
bgColor = "red"
lightColor = "#3e7fef"
activeColor = "#2b2b2b"
workingColor = "#ab1bd3"
errorColor = "#f4494f"
successColor = "#15a534"
reliefStyle = "flat"

with open(parentDir + "\\src\\theme.py") as themefile:
    themecont = themefile.readlines()
    for line in themecont:
        exec(line)


def settingChangesInfo():
    settingsWin = tk.Tk()
    settingsWin.destroy()
    changesReminder = tk.Label(settingsWin, text="The settings will apply at the next program start.", font=('Calibri Light', 10), bg=activeColor, fg=fgColor)
    changesReminder.pack()

def chunkDlButtonClicked():
    settingChangesInfo()

def settingsopen():
    print("SETTINGS")

    settingsWin = tk.Tk()
    settingsWin.title(winTitle)
    settingsWin["bg"] = bgColor

    settingsTitle = tk.Label(settingsWin, text="MCTools Settings", font=('Calibri Light', 30), bg=bgColor, fg=fgColor)
    settingsTitle.pack()

    designTitle = tk.Label(settingsWin, text="Design", font=('Calibri Light', 25), bg=bgColor, fg=lightColor)
    designTitle.pack()

    themeTitle = tk.Label(settingsWin, text="Theme", font=('Calibri Light', 20), bg=bgColor, fg=fgColor)
    themeTitle.pack()

    designTitle = tk.Label(settingsWin, text="Download", font=('Calibri Light', 25), bg=bgColor, fg=lightColor)
    designTitle.pack()

    doChunkdl = tk.IntVar()

    designTitle = tk.Checkbutton(settingsWin, text="Chunk download", font=('Calibri Light', 20), bg=bgColor, fg=fgColor, variable=doChunkdl, onvalue=1, offvalue=0, command=chunkDlButtonClicked)
    designTitle.pack()
    
    settingsWin.mainloop()