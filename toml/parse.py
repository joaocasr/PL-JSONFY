import tomyacc
import sys
import json


def call(path):
    with open(path,'r') as file:
        toml = file.read()

    result = tomyacc.parser.parse(toml)  
    #print(result)
    #jsonobj = json.loads(result)
    jsonobj=json.dumps(result,indent=4,ensure_ascii=False)

    path = path.replace(".toml", ".json")

    with open(path, "w",encoding='utf-8') as outfile:
            outfile.write(jsonobj)  

    print(jsonobj)