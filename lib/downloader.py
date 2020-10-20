import main

import os
import time
import tkinter
import requests
from tkinter import messagebox # because getting AttributeErrors without

print(f"DL\tloaded sucessfully @{__name__}")

downloadName = ""

def download(url):
    global downloadName
    print("DOWNLOADNAME \t" + downloadName)
    if downloadName == "":
        x = url.split("/")
        downloadName = x[-1]
    print("FILENAME\t" + downloadName)

    main.exe(x="dlBtn['state'] = 'disabled'")
    main.exe(x='dlBtn["text"] = "Downloading..."')
    main.exe(x='urlInp["bg"] = workingColor')

#try:
    main.exe(x='win.title("Downloading...")')
    myfile = requests.get(url)
    main.exe(x='urlInp["bg"] = successColor')

#try:
    infoTitle ="f'Installing {round(len(myfile.content)/1_048_576, 2)} mb ...'"
    main.exe(x=f'win.title({infoTitle})')
    main.exe(x=f'dlBtn["text"] = {infoTitle}')
    installpath = f"{os.getenv('APPDATA')}\\.minecraft\\resourcepacks\\{downloadName}.zip"
    installpath = installpath.replace('\\','/')
    print("INSTALLPATH\t" + installpath)
    try:
        open(installpath, "wb").write(myfile.content)
    except FileNotFoundError:
        messagebox.showerror(title="Invalid install path", message=f"Couldn't install the file because the Minecraft path is invalid")

    install_kb = len(myfile.content)/1_048_576
    rd_instkb = round(install_kb, 2)
    main.exe(x=f'win.title("Installed {rd_instkb} mb.")')
    main.exe(x='urlInp["bg"] = successColor')
    time.sleep(1)
    main.exe(x='urlInp.delete(0, "end")')
    main.exe(x='urlInp["bg"] = bgColor')

#except:
    main.exe(x='urlInp["bg"] = errorColor')
    main.exe(x='tk.messagebox.showerror(title="ERROR", message="could not install")')

#except:
    main.exe(x='urlInp["bg"] = errorColor')
    main.exe(x='tk.messagebox.showerror(title="ERROR", message="instable connection to url")')

    #finally:
        #main.exe(x='urlInp.delete(0, "end")')

    main.exe(x="dlBtn['state'] = 'normal'")