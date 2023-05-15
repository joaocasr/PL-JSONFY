import tomlex
import sys
import json


def call(path):
    with open(path,'r') as file:
        toml = file.read()

    tomlex.lexer.input(toml)
    while tok:=tomlex.lexer.token():
        print(tok)
        pass
    result = tomlex.parser.parse(toml)  
    #print(result)
    #jsonobj = json.loads(result)
    jsonobj=json.dumps(result,indent=4,ensure_ascii=False)

    path = path.replace(".toml", ".json")

    with open(path, "w",encoding='utf-8') as outfile:
            outfile.write(jsonobj)  

    print(jsonobj)