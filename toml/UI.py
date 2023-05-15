import requests
import subprocess
import parse

title = "|" + "-"*10 + "PL-JSONFY UI" + "-"*10 + "|"

print(title)
fp = input("Introduce TOML Pathname > ")
parse.call(fp)
fp = fp.replace(".toml", "json")
serverProc = subprocess.Popen(["json-server", "--watch", fp])

