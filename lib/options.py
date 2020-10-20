import main

import os
import tkinter
from tkinter import messagebox # because getting AttributeErrors without

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
    print("SETTINGCHANGEINFO")
    tkinter.messagebox.askyesno(title="Restart to apply?", message=f"The settings will apply at the next program start. Do you wish to restart the program now?")

def chunkDlButtonClicked():
    print("SETTINGS\tchanged")
    settingChangesInfo()

def aquaTheme():
    settingChangesInfo()

def open():
    print("SETTINGS")

    settingsWin = tkinter.Tk()
    settingsWin.title(winTitle)
    settingsWin["bg"] = bgColor

    settingsTitle = tkinter.Label(settingsWin, text="MCTools Settings", font=('Calibri Light', 30), bg=bgColor, fg=fgColor)
    settingsTitle.pack()

    designTitle = tkinter.Label(settingsWin, text="Design", font=('Calibri Light', 25), bg=bgColor, fg=lightColor)
    designTitle.pack()

    aquaThemeBtn = tkinter.Button(settingsWin, text="Blue (Default)", command=aquaTheme, font=('Calibri Light', 15), bg=bgColor, fg=fgColor, relief=reliefStyle, activebackground=activeColor)
    aquaThemeBtn.pack()

    aquaThemeBtn = tkinter.Button(settingsWin, text="Purple", command=aquaTheme, font=('Calibri Light', 15), bg=bgColor, fg=fgColor, relief=reliefStyle, activebackground=activeColor)
    aquaThemeBtn.pack()

    designTitle = tkinter.Label(settingsWin, text="Download", font=('Calibri Light', 25), bg=bgColor, fg=lightColor)
    designTitle.pack()
    
    doChunkdl = tkinter.IntVar()
    designTitle = tkinter.Checkbutton(settingsWin, text="[Beta] Chunk download", font=('Calibri Light', 20), bg=bgColor, fg="white", variable=doChunkdl, onvalue=1, offvalue=0, command=chunkDlButtonClicked)
    designTitle.pack()
    
    settingsWin.mainloop()