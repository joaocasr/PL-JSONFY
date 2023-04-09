import re
import json


allgroups = dict()
leveldDict = dict()

with open('example.toml','r') as f:
    toml = f.read()

#Search for line with breaks
lista = re.search(r'[a-zA-Z]+\w\s?=\s?\[\n?(\"\w+\",?\n?)*\n?\]',toml)

#Replace multilines list into one line list
onelinelist = lista.group(0).replace("\n","")
tom = re.sub(r'[a-zA-Z]+\w\s?=\s?\[\n?(\"\w+\",?\n?)*\n?\]',onelinelist,toml)

lista = re.findall(r'\[([a-zA-Z]+(.\w+)*)\]\n(?P<group>((\w|#|").*\n*)+)',tom)

lista2 = re.findall(r'(([a-zA-Z].+\n)+)',tom)
header=lista2[0][0]
lheaders = header.split("\n")

print(lheaders)
for p in lista:
    allgroups[p[0]] = p[2].strip()


def dicjoin(origindict, secdict):
    for (k,v) in secdict.items():
        if (k in origindict and isinstance(origindict[k], dict) and isinstance(secdict[k], dict)): 
            dicjoin(origindict[k], secdict[k])
        else:
            origindict[k] = secdict[k]

def getNestedDict(lista,value):
    treedict = value
    for k in reversed(lista):
        treedict = {k: treedict}
    return treedict

#print(getNestedDict(['b','v','c'],{"l":1}))
def convert_dict(lista):
    aux = {}
    for v in lista:
        if(len(v)>0):
            if("#" in v):
                continue
            atrib = v.split("=")[0]
            if("\"" in v): value = v.split("=")[1].replace("\"","")
            elif("\"" not in v and "=" in v): value = v.split("=")[1]
            if(value[0]==" "): value=value.lstrip()
            if(value[0]=="["):
                value = value.strip('][').split(',')
                n=0
                while(n<len(value)):
                    value[n]=value[n].strip()
                    n=n+1
                if(value[0].isnumeric()):
                    n=0
                    while(n<len(value)):
                        value[n]=int(value[n])
                        n=n+1
                aux.update({atrib:value})
            elif(value.isnumeric()):
                aux.update({atrib:int(value)})
            elif(value=="false" or value=="true"):
                aux.update({atrib:bool(value)})
            else:
                aux.update({atrib:value})
    return aux

dic = {}
dicjoin(dic,convert_dict(lheaders))

for p in allgroups:
    lista = p.split(".")
    if(len(lista)>1):
        nested=getNestedDict(lista,convert_dict(allgroups[p].split("\n")))
        dicjoin(dic,nested)
    else:
        dic.update({lista[0]:convert_dict(allgroups[lista[0]].split("\n"))})


jobj = json.dumps(dic, indent=4)

with open("jsonfy.json", "w") as outfile:
    outfile.write(jobj)
