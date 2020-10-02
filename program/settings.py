import main

import tkinter as tk

main.settheme()

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