import main

import os
import json
import tkinter as tk
import requests as rq

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

with open(parentDir + "\\src\\theme.py") as themefile:
    themecont = themefile.readlines()
    for line in themecont:
        exec(line)

try:
    lstweb = rq.get("https://pastebin.com/raw/gJndewWa")
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
        
# Set command for download button press
j=6
downloadName = ""
for q in range(len(lst)):
    exec(f"def dlNo{q}():\n\tdownloadName = lst[{q}][{0}] + '-' + str(lst[{q}][{1}]) + '-' + str(lst[{q}][{2}]) + 'x'\n\tmain.downloadTable(url=lst[{q}][{j}], dlN=downloadName)")
    print(f"COMMANDRANGE\t{q}")

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