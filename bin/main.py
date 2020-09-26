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
activeColor = "#2b2b2b"
workingColor = "#ab1bd3"
errorColor = "#f4494f"
successColor = "#15a534"
reliefStyle = "flat"

# Windows configuration
win = tk.Tk()
win.title(winTitle)
win.config(bg=bgColor)

building = False

def download(url):
    x = url.split("/")
    filename = x[-1]
    print("FILENAME\t" + filename)
    dlBtn['state'] = 'disabled'
    urlInp["bg"] = workingColor

    try:
        win.title("Downloading...")
        myfile = rq.get(url)
        urlInp["bg"] = successColor

        try:
            win.title(f"Installing {round(len(myfile.content)/1_048_576, 2)} mb ...")
            installpath = f"{os.getenv('APPDATA')}\\.minecraft\\resourcepacks\\{filename}"
            print("INSTALLPATH\t" + installpath)
            open(installpath, "wb").write(myfile.content)

            install_kb = len(myfile.content)/1_048_576
            rd_instkb = round(install_kb, 2)
            win.title(f"Installed {rd_instkb} mb.")
            urlInp["bg"] = successColor

        except:
            urlInp["bg"] = errorColor
            tk.messagebox.showerror(title="ERROR", message="could not install")

    except:
        urlInp["bg"] = errorColor
        tk.messagebox.showerror(title="ERROR", message="instable connection to url")

    finally:
        urlInp.delete(1)

    dlBtn['state'] = 'normal'

def downloadThread():
    dlTr = tr.Thread(target=download(url=urlInp.get()))
    dlTr.start()

def tableopen():
    # Create texturepack list
    class Table: 
        
        def __init__(self, tablewin):
            def downloadTable(url):
                print("I\t" + str(i))
                print("J\t" + str(j))
                print("TABLESELECT\t" + lst[i][j])
                print("DOWNLOADURL\t")

                tablewin.destroy()
                urlInp.delete(1)
                urlInp.insert("end", url)
                downloadThread()

            building = True
            info = ["Name", "Version", "Pixels", "Style"]

            for x in range(4):
                self.e = tk.Label(tablewin, text=info[x], fg=fgColor, bg=bgColor, font=('Calibri Light', 16, 'bold'), relief=reliefStyle)
                self.e.grid(row=0, column=x)

            for i in range(total_rows):
                for j in range(total_columns):
                    if j == 4:
                        self.e = tk.Button(tablewin, text="Install", width=10, fg=lightColor, bg=bgColor, font=('Calibri Light', 16, 'bold'), relief=reliefStyle, activebackground=activeColor)
                        self.e["command"] = lambda: downloadTable(url=lst[i][4]) 
                        self.e.grid(row=i+1, column=j)
                    
                    elif j == 0:
                        self.e = tk.Label(tablewin, text=lst[i][j], width=10, fg=fgColor, bg=bgColor, font=('Calibri Light', 16, 'bold'), relief=reliefStyle) 
                        self.e.grid(row=i+1, column=j) 

                    else:
                        self.e = tk.Label(tablewin, text=lst[i][j], width=10, fg=fgColor, bg=bgColor, font=('Calibri Light', 16), relief=reliefStyle) 
                        self.e.grid(row=i+1, column=j)
                
            building = False


    lst = [["Faithful","1.16.3","32","vanilla","https://github.com/seirin-blu/Faithful/raw/releases/Faithful-1.16.3.zip"],["Faithful","1.14","32","vanilla","https://raw.githubusercontent.com/FaithfulTeam/Faithful/releases/1.14.zip"],["Faithful","1.12","32","vanilla","https://github.com/FaithfulTeam/Faithful/raw/releases/1.12.zip"],["Faithful","1.8","32","vanilla","https://static.planetminecraft.com/files/resource_media/texture/faithful-1-8-for-pvp.zip"]]

    total_rows = len(lst) 
    total_columns = len(lst[0]) 

    tablewin = tk.Tk()
    tablewin.config(bg=bgColor)
    tablewin.title("Texturepack Table")
    t = Table(tablewin) 
    tablewin.mainloop() 

titleTxt = tk.Label(win, text="Styx MCTools", font=('Calibri Light', 50), bg=bgColor, fg=fgColor)
titleTxt.pack()

tableBtn = tk.Button(win, text="Open texturepacks", command=tableopen, font=('Calibri Light', 0), bg=bgColor, fg=lightColor, relief=reliefStyle, activebackground=activeColor)
tableBtn.pack()

urlInp = tk.Entry(win, font=('Calibri Light', 0), bg=bgColor, fg=fgColor, relief="groove")
urlInp.pack()

dlBtn = tk.Button(win, text="Install from url", command=downloadThread, font=('Calibri Light', 0), bg=bgColor, fg=fgColor, relief=reliefStyle, activebackground=activeColor)
dlBtn.pack()

win.mainloop()