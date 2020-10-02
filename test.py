import os

parentDir = os.path.dirname(os.path.abspath(__file__))

with open(parentDir + "\\src\\theme.py") as themefile:
    themecont = themefile.readlines()
    for line in themecont:
        exec(line)