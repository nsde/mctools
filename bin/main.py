import os
import tkinter as tk
import requests as rq
import threading as tr
from tkinter import messagebox

# Program settings
winTitle = "Styx MCTools"
defaultFiletype = ".zip"

# Theme settings
fgColor = "white"
bgColor = "#212121"
lightColor = "#3e7fef"
activeColor = "#3f3f3f"
errorColor = "#f4494f"
successColor = "#15a534"
reliefStyle = "flat"

# Windows configuration
win = tk.Tk()
win.title(winTitle)
win.config(bg=bgColor)

def download():
    url = urlInp.get()
    x = url.split("/")
    filename = x[-1]
    dlBtn['state'] = 'disabled'

    try:
        win.title("Downloading...")
        myfile = rq.get(url)
        urlInp["bg"] = successColor

        try:
            win.title(f"Installing {round(len(myfile.content)/1_048_576, 2)} mb ...")
            installpath = f"{os.getenv('APPDATA')}\\.minecraft\\resourcepacks\\{filename}"
            print(installpath)
            open(installpath, "wb").write(myfile.content)
            win.title(f"Installed {round(len(myfile.content)/1_048_576, 2)} mb.'

            urlInp["bg"] = successColor

        except:
            urlInp["bg"] = errorColor
            tk.messagebox.showerror(title="ERROR", message="could not install")

    except:
        urlInp["bg"] = errorColor
        tk.messagebox.showerror(title="ERROR", message="instable connection to url")
    
    dlBtn['state'] = 'normal'

def downloadClicked():
    dlTr = tr.Thread(target=download)
    dlTr.start()

titleTxt = tk.Label(win, text="Styx MCTools", font=('Calibri Light', 50), bg=bgColor, fg=fgColor)
titleTxt.pack()

urlInp = tk.Entry(win, font=('Calibri Light', 0), bg=bgColor, fg=fgColor, relief="groove")
urlInp.pack()

dlBtn = tk.Button(win, text="Start", command=downloadClicked, font=('Calibri Light', 0), bg=bgColor, fg=fgColor, relief=reliefStyle, activebackground=activeColor)
dlBtn.pack()

win.mainloop()