appVersion = 1

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

# Theme settings
fgColor = "white"
bgColor = "#212121"
lightColor = "#3e7fef"
activeColor = "#2b2b2b"
workingColor = "#ab1bd3"
errorColor = "#f4494f"
successColor = "#15a534"
reliefStyle = "flat"

# Windows configuration
win = tk.Tk()

tablewin = tk.Tk()
tablewin.destroy()

fileDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.dirname(fileDir)

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
try:
    lstweb = rq.get("https://raw.githubusercontent.com/nsde/files/master/texturepacks/list.py")
    lst = lstweb.text
    lst = json.loads(lst)
    print(lst)

except: # no connection etc.
    # demo for testing
    print("CONNECTION ERROR")
    lst=[
            ["Default","1.0","1","DEMO","0","google.com","https://google.com/"],
            ["Default","1.0","2","DEMO","0","google.com","https://google.com/"],
            ["Default","1.0","3","DEMO","0","google.com","https://google.com/"]
        ]

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

# Set command for download button press
j=6
for q in range(len(lst)):
    exec(f"def dlNo{q}():\n\tdownloadName = lst[{q}][{0}] + '-' + str(lst[{q}][{1}]) + '-' + str(lst[{q}][{2}]) + 'x'\n\tdownloadTable(url=lst[{q}][{j}], dlN=downloadName)")

# Set command for webpage open
j=5
for q in range(len(lst)):
    exec(f"def webP{q}():\n\tweb.open('https://{lst[q][j]}', autoraise=True)")


def tableopen():
    print("GENERATE TABLE")
    # Create texturepack list
    class Table: 
        
        def __init__(self, tablewin):
            info = ["Name", "Version", "Pixels", "Style", "Download"]

            for x in range(len(info)):
                self.e = tk.Label(tablewin, text=info[x], fg=fgColor, bg=bgColor, font=('Calibri Light', 16, 'bold', 'underline'), relief=reliefStyle)
                self.e.grid(row=0, column=x)

            for i in range(total_rows):
                for j in range(total_columns):
                    print("BUILDING\ti "+str(i)+"\t j "+str(j))
                    if j == 4:
                        self.e = tk.Button(tablewin, text=lst[i][4] + 'mb', width=10, fg=workingColor, bg=bgColor, font=('Calibri Light', 16, 'bold'), relief=reliefStyle, activebackground=activeColor)
                        exec('self.e["command"] = dlNo' + str(i))
                        print('EXEC\tself.e["command"] = dlNo' + str(i))
                        self.e.grid(row=i+1, column=j)

                    elif j == 5 or j == 6:
                        print("BREAK")
                        break

                    elif j == 0:
                        self.e = tk.Button(tablewin, text=lst[i][j], width=10, fg=lightColor, bg=bgColor, font=('Calibri Light', 16, 'bold'), relief=reliefStyle) 
                        exec('self.e["command"] = webP' + str(i))
                        print('EXEC\tself.e["command"] = webP' + str(i))
                        self.e.grid(row=i+1, column=j)

                    else:
                        self.e = tk.Label(tablewin, text=lst[i][j], width=10, fg=fgColor, bg=bgColor, font=('Calibri Light', 16), relief=reliefStyle) 
                        self.e.grid(row=i+1, column=j)
                
    total_rows = len(lst) 
    total_columns = len(lst[0]) 

    tablewin = tk.Tk()
    tablewin.config(bg=bgColor)
    tablewin.title("Texturepacks")
    t = Table(tablewin) 
    tablewin.mainloop() 

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
    print("SETTINGS")
    settingsWin = tk.Tk()
    settingsWin.title(winTitle)
    settingsWin["bg"] = bgColor

    settingsTitle = tk.Label(settingsWin, text="MCTools Settings", font=('Calibri Light', 30), bg=bgColor, fg=fgColor)
    settingsTitle.pack()

    themeTitle = tk.Label(settingsWin, text="Design", font=('Calibri Light', 20), bg=bgColor, fg=lightColor)
    themeTitle.pack()

    settingsWin.mainloop()

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