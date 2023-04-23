import tomlex
import sys
import json

with open('example.toml','r') as file:
    toml = file.read()


tomlex.lexer.input(toml)
while tok:=tomlex.lexer.token():
    print(tok)
    pass
result = tomlex.parser.parse(toml)  
#print(result)
#jsonobj = json.loads(result)
jsonobj=json.dumps(result,indent=4,ensure_ascii=False)

with open("jsonfy.json", "w",encoding='utf-8') as outfile:
        outfile.write(jsonobj)
print(jsonobj)
