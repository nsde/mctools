# -*- coding: utf-8 -*-

appVersion = 2

import settings
import downloader
import texturepacks

import os
import sys
import tkinter
import requests
import threading
import webbrowser as web
from tkinter import messagebox # because getting AttributeErrors without


# Execute function
def exe(x):
    exec(x)

# Program settings
winTitle = "Styx MCTools"
defaultFiletype = ".zip"
downloadName = ""

# Path settings
fileDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.dirname(fileDir)

# Theme settings
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
            
# Windows configuration
win = tkinter.Tk()
print(f"STARTED\tby @{__name__}")

if __name__ == "__main__":
    win.destroy()

winIcon = tkinter.PhotoImage(file = parentDir + '\\src\\main.png')
win.title(winTitle)
win.config(bg=bgColor)
win.iconphoto(False, winIcon)

print("UPDATE CHECKER")
try:
    updc = requests.get("https://raw.githubusercontent.com/nsde/files/master/texturepacks/appversion")
    newestVersion = int(updc.text)

    if appVersion != newestVersion:
        if tkinter.messagebox.askokcancel(title="Version outdated", message=f"Version {newestVersion} avaiable. Do you want to download it?"):
            web.open("https://github.com/nsde/mctools/releases/")

except:
    print("CHECK FOR NEWEST VERSION FAILED")
    win.title("No internet connection")

# Load list of texturepacks

def downloadThread():
    dlTr = threading.Thread(target=downloader.download(url=urlInp.get()))
    dlTr.start()

def downloadTable(url, dlN):
    global downloadName
    downloadName = dlN

    win.attributes("-topmost", True)
    print("DOWNLOADURL\t" + url)

    urlInp.delete(0, "end")
    urlInp.insert("end", url)
    print("STARTING DLTHREAD")
    downloadThread()
    return downloadName

print("GENERATE COMMANDS")

def tableopen():
    texturepacks.tableopen()

def tablethread():
    tabletr = threading.Thread(target=tableopen)
    tabletr.start()

def exitapp():
    print("BYE!")
    sys.exit(0)

def gh():
    print("GITHUB")
    web.open("https://github.com/nsde/mctools")

def doSettingsOpen():
    settings.open()

print("GENERATE GUI")

titleTxt = tkinter.Label(win, text="Styx MCTools", font=('Calibri Light', 50), bg=bgColor, fg=fgColor)
titleTxt.pack()

tableBtn = tkinter.Button(win, text="Resourcepacks", command=tablethread, font=('Calibri Light', 20), bg=bgColor, fg=lightColor, relief=reliefStyle, activebackground=activeColor)
tableBtn.pack()

urlInp = tkinter.Entry(win, font=('Calibri Light', 0), bg=bgColor, fg=fgColor, relief="groove")
urlInp.pack()

dlBtn = tkinter.Button(win, text="Install", command=downloadThread, font=('Calibri Light', 20), bg=bgColor, fg=fgColor, relief=reliefStyle, activebackground=activeColor)
dlBtn.pack()

ghBtn = tkinter.Button(win, text="Information", command=gh, font=('Calibri Light', 15), bg=bgColor, fg=fgColor, relief=reliefStyle, activebackground=activeColor)
ghBtn.pack()

settingsBtn = tkinter.Button(win, text="Settings", command=doSettingsOpen, font=('Calibri Light', 15), bg=bgColor, fg=fgColor, relief=reliefStyle, activebackground=activeColor)
settingsBtn.pack()


print("MAINLOOP")
win.mainloop()
print("IN MAINLOOP")