import tomlex
import sys
import json
#from converter import converter


with open('/home/joao/PL-JSONFY/example.toml','r') as file:
    toml = file.read()

tomlex.lexer.input(toml)
while tok:=tomlex.lexer.token():
    print(tok)
    pass
result = tomlex.parser.parse(toml)  
print(result)
