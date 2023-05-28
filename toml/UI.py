import requests
import subprocess
import parse
from os import getcwd
from webbrowser import open as wbOpen
from requests import get as rGet

title = "|" + "-"*10 + "PL-JSONFY UI" + "-"*10 + "|"
mMenu = """1) Open in Browser
0) Exit""" 

print(title)
print("1) JSON-Server Compatible\n2) Print Output")
op = int(input(">> "))
fp = input("Introduce TOML Pathname >> ")
parse.call(fp)
fp = fp.replace(".toml", ".json")
fp = getcwd() + "\\" + fp

if op == 1:
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
