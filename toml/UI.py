import requests
import subprocess
import parse
from os import getcwd
from webbrowser import open as wbOpen
from sys import platform

title = "|" + "-"*10 + "PL-JSONFY UI" + "-"*10 + "|"
mMenu = """1) Open in Browser
0) Exit""" 

print(title)
print("1) JSON-Server Compatible\n2) Print Output")
op = int(input(">> "))
fp = input("Introduce TOML Pathname >> ")
if platform == "linux" or platform == "linux2":
    fp = getcwd() + "/" + fp
elif platform == "darwin":
    fp = getcwd() + "/" + fp
elif platform == "win32":
    fp = getcwd() + "\\" + fp

parse.call(fp)
fp = fp.replace(".toml", ".json")

if op == 1:
    if platform == "linux" or platform == "linux2":
        print(fp)
        subprocess.run(["json-server", "-w", fp], shell=True, stdout=subprocess.DEVNULL,
                                  stderr=subprocess.DEVNULL)
    elif platform == "darwin":
        subprocess.run(["json-server", "--watch", fp], shell=True, stdout=subprocess.DEVNULL,
                                  stderr=subprocess.DEVNULL)
    elif platform == "win32":
        serverProc = subprocess.Popen(["json-server", "--watch", fp], shell=True, 
                                  stdout=subprocess.DEVNULL)
        
    while 1:
        print(title)
        print(mMenu)

        x = int(input(">> "))
        if x == 0:
            serverProc.kill()
            break
        if x == 1:
            wbOpen("http://localhost:3000", new=0, autoraise=True)
