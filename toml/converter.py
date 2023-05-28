def upperdic(d, keys=[]):
    if not isinstance(d, dict):
        return keys, d
    kval = []
    for key in d:
        nested_keys, nested_value = upperdic(d[key], keys + [key])
        kval.append((nested_keys, nested_value))
    return max(kval, key=lambda pair: len(pair[0]))

def insertLast(dictionary, new):
    keys, d = upperdic(dictionary)
    currentdict = dictionary
    for k in keys[0:len(keys)-1]:
        currentdict = currentdict[k]
    if(type(currentdict[keys[-1]]) is list):
        currentdict[keys[-1]].append(new)
    else:
        currentdict[keys[-1]]=new


def fusion(origindict, secdict):
    for (k,v) in secdict.items():
        if (k in origindict and isinstance(origindict[k], dict) and isinstance(secdict[k], dict)):
            fusion(origindict[k], secdict[k])
        elif k in origindict and isinstance(origindict[k], list) and isinstance(secdict[k],list):
            if(len(origindict[k])>=1):
                size =len(secdict[k])
                i=0
                while(i<size):
                    origindict[k].append(secdict[k][i])
                    i+=1    
            else:
                origindict[k].append(secdict[k])
        else:
            origindict[k] = secdict[k]

