import main

import os
import tkinter

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

chunkDlsetting = 0

with open(parentDir + "\\src\\theme.py") as themefile:
    themecont = themefile.readlines()
    for line in themecont:
        exec(line)


def settingChangesInfo():
    settingsWin = tkinter.Tk()
    settingsWin.destroy()
    changesReminder = tkinter.Label(settingsWin, text="The settings will apply at the next program start.", font=('Calibri Light', 10), bg=activeColor, fg=fgColor)
    changesReminder.pack()

def chunkDlButtonClicked():
    print("SETTINGS\tchanged")
    settingChangesInfo()

def settingsopen():
    print("SETTINGS")

    settingsWin = tkinter.Tk()
    settingsWin.title(winTitle)
    settingsWin["bg"] = bgColor

    settingsTitle = tkinter.Label(settingsWin, text="MCTools Settings", font=('Calibri Light', 30), bg=bgColor, fg=fgColor)
    settingsTitle.pack()

    designTitle = tkinter.Label(settingsWin, text="Design", font=('Calibri Light', 25), bg=bgColor, fg=lightColor)
    designTitle.pack()

    themeTitle = tkinter.Label(settingsWin, text="Theme", font=('Calibri Light', 20), bg=bgColor, fg=fgColor)
    themeTitle.pack()

    designTitle = tkinter.Label(settingsWin, text="Download", font=('Calibri Light', 25), bg=bgColor, fg=lightColor)
    designTitle.pack()

    doChunkdl = tkinter.IntVar()

    designTitle = tkinter.Checkbutton(settingsWin, text="Chunk download", font=('Calibri Light', 20), bg=bgColor, fg=lightColor, variable=doChunkdl, onvalue=1, offvalue=0, command=chunkDlButtonClicked)
    designTitle.pack()
    
    settingsWin.mainloop()