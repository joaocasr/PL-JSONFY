# JSONfy

JSONfy is a tool that reads TOML input data and converts it to JSON format.
This tool was built with lex and yacc submodules from ply.
In each GIC semantic action, data structures such as dictionaries and lists were manipulated in order to produce the resulting JSON.

For more information go to TOML documentation: https://github.com/toml-lang/toml

## How to use it

Add your TOML files in the Tests folder. While running the program, option 1) will allow the resulting JSON to be consumed by Json Server, which is a library that simulates a RESTFUL API. Therefore the input must be compatible with the data format that the Json Server can handle.
Option 2) will output the transformed data and will produce a JSON file.
1. Go to PL-JSONFY folder.
2. Write the following command on the terminal in the directory PL-JSONFY/ :
```
pyhon toml/UI.py
```
3. Select one of the following options
```
1) JSON-Server Compatible
2) Print Output
```
4. Write the pathname from your TOML file. eg.:
```
Tests/test1.toml
```

## Development Team
This project was developed by the following members:

- João Castro
- Tomás Dias
- Renato Gomes

# Example
- Generic toml file with all data types and TOML structures.

```toml
title = "TOML Example"
title2 = "random title"
v = 1
name = "Tom Preston Werner"
[raios]
new_string="novinho"
lines = '''
The first newline is
trimmed in raw strings.
   All other whitespace
   is preserved.
'''
str3 = """\
       The quick brown \
       fox jumps over \
       the lazy dog\
       """

[homem]
teofilo="barraca"
flt1 = +1.0
flt2 = 3.1415
flt3 = -0.01

# exponent
flt4 = 5e+22
flt5 = 1e06
flt6 = -2E-2

# both
flt8 = 224_617.445_991_228

[meu]
server = "I'm a string. \"You can quote me\". Name\tJos\u00E9."
siu= [ 1, 3,[ "ola", "filho"], 5]
message="\u0068\u0065\u006c\u006c\u006f \u0077\u006f\u0072\u006c\u0064"

[meu.nome]
ok=true
pergunta= "porque"
[meu.nome.fixe]
esfincter= 23
nome ="joao"
time = 1979-05-27T07:32:00Z
time2 = 1979-05-27
str4 = """Here are two quotation marks: "". Simple enough."""
str5 = """Here are three quotation marks: ""\"."""
str6 = """Here are fifteen quotation marks: ""\"""\"""\"""\"""\"."""

# This is a pointless statement
str7 = """"This," she said, "is just a pointless statement"."""
winpath = 'C:\Users\nodejs\templates'
str = ''''That,' she said, 'is still pointless'.'''

name = { first = "Tom", last = "Preston-Werner" }
point = { x = 1, y = 2 }
animal = { type.name = "pug" }

[[blog.posts.entry.tags]]
name = "tag1"

[[blog.posts.entry.tags]]
name = "tag2"

[[blog.posts.entry.comments]]
author = "John"
text = "Great post"

[[blog.posts.entry.comments]]
author = "Jane"
text = "Interesting read"
```

- Final JSON output file:
```json
{
    "title": "TOML Example",
    "title2": "random title",
    "v": 1,
    "name": "Tom Preston Werner",
    "raios": {
        "new_string": "novinho",
        "lines": "The first newline is\ntrimmed in raw strings.\n   All other whitespace\n   is preserved.\n",
        "str3": "The quick brown fox jumps over the lazy dog"
    },
    "homem": {
        "teofilo": "barraca",
        "flt1": 1.0,
        "flt2": 3.1415,
        "flt3": -0.01,
        "flt4": 5e+22,
        "flt5": 1000000.0,
        "flt6": -0.02,
        "flt8": 224617.445991228
    },
    "meu": {
        "server": "I'm a string. \"You can quote me\". Name\tJosé.",
        "siu": [
            1,
            3,
            [
                "ola",
                "filho"
            ],
            5
        ],
        "message": "hello world",
        "nome": {
            "ok": true,
            "pergunta": "porque",
            "fixe": {
                "esfincter": 23,
                "nome": "joao",
                "time": "1979-05-27T07:32:00Z",
                "time2": "1979-05-27",
                "str4": "Here are two quotation marks: \"\". Simple enough.",
                "str5": "Here are three quotation marks: \"\"\".",
                "str6": "Here are fifteen quotation marks: \"\"\"\"\"\"\"\"\"\"\"\"\"\"\".",
                "str7": "\"This,\" she said, \"is just a pointless statement\".",
                "winpath": "C:\\Users\\nodejs\templates",
                "str": "'That,' she said, 'is still pointless'.",
                "name": {
                    "first": "Tom",
                    "last": "Preston-Werner"
                },
                "point": {
                    "x": 1,
                    "y": 2
                },
                "animal": {
                    "type": {
                        "name": "pug"
                    }
                }
            }
        }
    },
    "blog": {
        "posts": {
            "entry": {
                "tags": [
                    {
                        "name": "tag1"
                    },
                    {
                        "name": "tag2"
                    }
                ],
                "comments": [
                    {
                        "author": "John",
                        "text": "Great post"
                    },
                    {
                        "author": "Jane",
                        "text": "Interesting read"
                    }
                ]
            }
        }
    }
}
```