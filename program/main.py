# -*- coding: utf-8 -*-

appVersion = 2

import tp
import settings

import os
import sys
import json
import tkinter as tk
import requests as rq
import threading as tr
from time import sleep
import webbrowser as web
from tkinter import messagebox

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
win = tk.Tk()
settingsWin = tk.Tk()
tablewin = tk.Tk()

tablewin.destroy()
settingsWin.destroy()

winIcon = tk.PhotoImage(file = parentDir + '\\src\\main.png')
win.title(winTitle)
win.config(bg=bgColor)
win.iconphoto(False, winIcon)

print("UPDATE CHECKER")
try:
    updc = rq.get("https://raw.githubusercontent.com/nsde/files/master/texturepacks/appversion")
    newestVersion = int(updc.text)

    if appVersion != newestVersion:
        if tk.messagebox.askokcancel(title="WARNING", message="There is a newer version avaiable. Do you want to download it?"):
            web.open("https://github.com/nsde/mctools/releases/")

except:
    print("CHECK FOR NEWEST VERSION FAILED")
    win.title("No internet connection")

# Load list of texturepacks


def download(url):
    global downloadName
    print("DOWNLOADNAME \t" + downloadName)
    if downloadName == "":
        x = url.split("/")
        downloadName = x[-1]
    print("FILENAME\t" + downloadName)
    dlBtn['state'] = 'disabled'
    urlInp["bg"] = workingColor

    try:
        win.title("Downloading...")
        myfile = rq.get(url)
        urlInp["bg"] = successColor

        try:
            win.title(f"Installing {round(len(myfile.content)/1_048_576, 2)} mb ...")
            installpath = f"{os.getenv('APPDATA')}\\.minecraft\\resourcepacks\\{downloadName}.zip"
            installpath = installpath.replace('\\','/')
            print("INSTALLPATH\t" + installpath)
            open(installpath, "wb").write(myfile.content)

            install_kb = len(myfile.content)/1_048_576
            rd_instkb = round(install_kb, 2)
            win.title(f"Installed {rd_instkb} mb.")
            urlInp["bg"] = successColor
            sleep(1)
            urlInp.delete(0, "end")
            urlInp["bg"] = bgColor

        except:
            urlInp["bg"] = errorColor
            tk.messagebox.showerror(title="ERROR", message="could not install")

    except:
        urlInp["bg"] = errorColor
        tk.messagebox.showerror(title="ERROR", message="instable connection to url")

    finally:
        urlInp.delete(0, "end")

    dlBtn['state'] = 'normal'

def downloadThread():
    dlTr = tr.Thread(target=download(url=urlInp.get()))
    dlTr.start()

def downloadTable(url, dlN):
    global downloadName
    downloadName = dlN

    win.attributes("-topmost", True)
    print("DOWNLOADURL\t" + url)

    try:
        tablewin.destroy()
    except:
        pass

    urlInp.delete(0, "end")
    urlInp.insert("end", url)
    print("STARTING DLTHREAD")
    downloadThread()
    return downloadName

print("GENERATE COMMANDS")

def tableopen():
    tp.tableopen()

def tablethread():
    tabletr = tr.Thread(target=tableopen)
    tabletr.start()

def exitapp():
    print("BYE!")
    sys.exit(0)

def gh():
    print("GITHUB")
    web.open("https://github.com/nsde/mctools")

def settingsopen():
    settings.settingsopen()

print("GENERATE GUI")

titleTxt = tk.Label(win, text="Styx MCTools", font=('Calibri Light', 50), bg=bgColor, fg=fgColor)
titleTxt.pack()

tableBtn = tk.Button(win, text="Open texturepacks", command=tablethread, font=('Calibri Light', 20), bg=bgColor, fg=lightColor, relief=reliefStyle, activebackground=activeColor)
tableBtn.pack()

urlInp = tk.Entry(win, font=('Calibri Light', 0), bg=bgColor, fg=fgColor, relief="groove")
urlInp.pack()

dlBtn = tk.Button(win, text="Install from url", command=downloadThread, font=('Calibri Light', 20), bg=bgColor, fg=fgColor, relief=reliefStyle, activebackground=activeColor)
dlBtn.pack()

ghBtn = tk.Button(win, text="Information", command=gh, font=('Calibri Light', 15), bg=bgColor, fg=fgColor, relief=reliefStyle, activebackground=activeColor)
ghBtn.pack()

ghBtn = tk.Button(win, text="Settings", command=settingsopen, font=('Calibri Light', 15), bg=bgColor, fg=fgColor, relief=reliefStyle, activebackground=activeColor)
ghBtn.pack()


print("MAINLOOP")

win.mainloop()