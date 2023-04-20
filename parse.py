import tomlex
import sys
import json

with open('/home/joao/PL-JSONFY/example.toml','r') as file:
    toml = file.read()


tomlex.lexer.input(toml)
while tok:=tomlex.lexer.token():
    #print(tok)
    pass
result = tomlex.parser.parse(toml)  
#print(result)
jsonobj = json.loads(result)
with open("jsonfy.json", "w") as outfile:
        json.dump(jsonobj,outfile,indent=4)
s=json.dumps(jsonobj,indent=4)
print(s)
