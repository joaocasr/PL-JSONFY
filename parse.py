import tomlex
import sys


with open('example.toml','r') as f:
    code = f.read()
    #print(code)
#LEXICAL ANALYSIS
#GRAMMAR ANALYSIS
#CONVERT TOML-> JSON

toml = '''time = 21:30:00
name = "Tom Preston-Werner"'''

tomlex.lexer.input(toml)
while tok:=tomlex.lexer.token():
    print(tok)
result = tomlex.parser.parse(toml)  
