import os
import main

import requests as rq

from time import sleep

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
    main.exe(x='urlInp["bg"] = workingColor')

#try:
    main.exe(x='win.title("Downloading...")')
    myfile = rq.get(url)
    main.exe(x='urlInp["bg"] = successColor')

#try:
    main.exe(x=f'win.title("Installing {round(len(myfile.content)/1_048_576, 2)} mb ...")')
    installpath = f"{os.getenv('APPDATA')}\\.minecraft\\resourcepacks\\{downloadName}.zip"
    installpath = installpath.replace('\\','/')
    print("INSTALLPATH\t" + installpath)
    open(installpath, "wb").write(myfile.content)

    install_kb = len(myfile.content)/1_048_576
    rd_instkb = round(install_kb, 2)
    main.exe(x=f'win.title("Installed {rd_instkb} mb.")')
    main.exe(x='urlInp["bg"] = successColor')
    sleep(1)
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