import ply.yacc as yacc
import converter

from tomlex import tokens

def p_TOML(p):
    "TOML : TITLES GROUPS"
    p[1].update(p[2])
    p[0]=p[1]    

def p_TITLES1(p): 
    "TITLES : KVALUE EXPRESSION TITLES"
    p[1].update(p[3])
    p[0]=p[1]
    
def p_TITLES2(p):
    "TITLES :"
    p[0] = {}

def p_GROUPS1(p):
    "GROUPS : SECCAO EXPRESSION GROUPS"
    converter.fusion(p[1],p[3])
    p[0]=p[1]

def p_GROUPS2(p):
    "GROUPS : "
    p[0] = {}

def p_SECCAO1(p):
    "SECCAO : TABLE EXPRESSION ATRIBUICOES"
    converter.insertLast(p[1],p[3])
    p[0]=p[1]


def p_SECCAO2(p):
    "SECCAO :"
    p[0] = {}

def p_ATRIBUICOES1(p):
    "ATRIBUICOES : KVALUE EXPRESSION ATRIBUICOES"
    p[1].update(p[3])
    p[0] = p[1]

def p_ATRIBUICOES2(p):
    "ATRIBUICOES :"
    p[0]={}    

def p_EXPRESSION1(p):
    "EXPRESSION : COMMENT EXPRESSION"
    pass

def p_EXPRESSION2(p):
    "EXPRESSION : NEWLINE EXPRESSION"
    pass

def p_EXPRESSION3(p):
    "EXPRESSION :"
    pass

def p_KVALUE(p):
    "KVALUE : KEY kvwhitespace IGUAL kvwhitespace VALUE"
    if type(p[1]) is dict:
        converter.insertLast(p[1],p[5])
        p[0] = p[1]
    else:
        p[0] = {p[1]:p[5]}

def p_kvwhitespace1(p):
    "kvwhitespace : WHITESPACE"
    pass

def p_kvwhitespace2(p):
    "kvwhitespace :"
    pass

def p_KEY1(p):
    "KEY : SIMPLEKEY"
    p[0] = p[1]    

def p_KEY2(p):
    "KEY : DOTKEY"
    p[0] = p[1]    
    

def p_SIMPLEKEY1(p):
    "SIMPLEKEY : QUOTEDKEY"    
    p[0] = p[1]    

def p_SIMPLEKEY2(p):
    "SIMPLEKEY : UNQUOTEDKEY"
    p[0] = p[1]    


def p_UNQUOTEDKEY1(p):
    "UNQUOTEDKEY : OCCURRENCES UNQUOTEDKEYAUX"
    p[0] = p[1] + p[2]    
    

def p_UNQUOTEDKEY2(p):
    "UNQUOTEDKEYAUX : OCCURRENCES UNQUOTEDKEYAUX"
    p[0] = p[1] + p[2]    
    

def p_UNQUOTEDKEY3(p):
    "UNQUOTEDKEYAUX :"
    p[0]=""    

def p_OCCURRENCES1(p):
    "OCCURRENCES : CHAR"
    p[0] = p[1] 

def p_OCCURRENCES2(p):
    "OCCURRENCES : INTEGER"
    p[0] = p[1] 
    

def p_OCCURRENCES3(p):
    "OCCURRENCES : MINUS"
    p[0] = p[1] 
    

def p_OCCURRENCES4(p):
    "OCCURRENCES : UNDERSCORE"
    p[0] = p[1] 
    

def p_QUOTEDKEY1(p):
    "QUOTEDKEY : BASICSTRING"
    p[0] = p[1] 
    

def p_QUOTEDKEY2(p):
    "QUOTEDKEY : LITERALSTRING"    
    p[0] = p[1] 

def p_DOTKEY(p):
    "DOTKEY : SIMPLEKEY DOT_SEP SIMPLEKEY DOTSIMPKEY"
    p[0] = {p[1]: {p[3]: p[4]}}

def p_DOTSIMPKEY1(p): 
    "DOTSIMPKEY : DOT_SEP SIMPLEKEY DOTSIMPKEY"
    p[0] = {p[2]: p[3]}
    

def p_DOTSIMPKEY2(p):
    "DOTSIMPKEY : "
    

def p_VALUE1(p):
    "VALUE : STRING"
    p[0] = p[1]


def p_VALUE2(p):
    "VALUE : BOOLEAN"
    p[0] = bool(p[1].capitalize())

def p_VALUE3(p):
    "VALUE : INTEGER"
    p[0] = int(p[1])    

def p_VALUE4(p):
    "VALUE : ARRAY"
    p[0] = list(p[1])    

def p_VALUE5(p):
    "VALUE : INLINETABLE"
    p[0] = p[1]
    

def p_VALUE6(p):
    "VALUE : DATETIME"
    p[0] = p[1]    

def p_DATETIME1(p):
    "DATETIME : LOCALDATETIME"
    p[0] = p[1]

def p_DATETIME2(p):
    "DATETIME : LOCALDATE"
    p[0] = p[1]

def p_DATETIME3(p):
    "DATETIME : LOCALTIME"
    p[0] = p[1]

def p_LOCALDATETIME(p):
    "LOCALDATETIME : LOCALDATE LOCALTIME"
    p[0] = p[1] + p[2]
    
def p_LOCALDATE(p):
    "LOCALDATE : DATE"
    p[0] = p[1]

def p_LOCALTIME(p):
    "LOCALTIME : TIME"
    p[0] = p[1]

def p_VALUE7(p):
    "VALUE : FLOAT"
    p[1]=float(p[1])
    p[0]=p[1]
    

def p_STRING1(p) : 
    "STRING : MULTILINEBASICSTRING"
    p[0]=p[1]


def p_STRING2(p) : 
    "STRING : BASICSTRING"
    p[0]=p[1]


def p_STRING3(p) : 
    "STRING : MLLITERALSTRING"
    p[0]=p[1]    

def p_STRING4(p) : 
    "STRING : LITERALSTRING"
    p[0]=p[1]
    

def p_BASICSTRING(p):
    "BASICSTRING : ASPA BC ASPA"
    p[0]= p[2]
    

def p_BC(p):
    "BC : BASICCHAR BC"
    p[0] = p[1] + str(p[2])

def p_BC2(p):
    "BC :"
    p[0]=""

def p_BASICCHAR1(p):
    "BASICCHAR : BASICUNESCAPED"
    p[0] = p[1]
    

def p_BASICCHAR2(p):
    "BASICCHAR : ESCAPED"
    p[0]= p[1]

def p_BASICUNESCAPED1(p):
    "BASICUNESCAPED : WHITESPACE"
    p[0]= p[1]

def p_BASICUNESCAPED2(p):
    "BASICUNESCAPED : CHAR"
    p[0] = p[1]

def p_BASICUNESCAPED3(p):
    "BASICUNESCAPED : INTEGER"
    p[0]= str(p[1])

def p_BASICUNESCAPED4(p):
    "BASICUNESCAPED : FLOAT"
    p[0]= str(p[1])

def p_BASICUNESCAPED5(p):
    "BASICUNESCAPED : MINUS"
    p[0] = p[1]

def p_BASICUNESCAPED6(p):
    "BASICUNESCAPED : APOSTROFE"
    p[0] = p[1]
    
def p_BASICUNESCAPED7(p):
    "BASICUNESCAPED : ESCAPED"
    p[0] = p[1]

def p_BASICUNESCAPED8(p):
    "BASICUNESCAPED : DOT_SEP"
    p[0]= p[1]

def p_BASICUNESCAPED9(p):
    "BASICUNESCAPED : TWODOT_SEP"
    p[0]= p[1]
    

################################
def p_ESCAPED1(p): 
    "ESCAPED : ESC_QUOTE"
    p[0]="\""
    

def p_ESCAPED2(p): 
    "ESCAPED : ESC_REVERSE"
    p[0]=p[1]


def p_ESCAPED3(p): 
    "ESCAPED : ESC_BACKSPACE"
    p[0]=p[1]
    

def p_ESCAPED4(p): 
    "ESCAPED : ESC_FF"
    p[0]=p[1]
    

def p_ESCAPED5(p): 
    "ESCAPED : ESC_NL"
    p[0]=p[1]
    

def p_ESCAPED6(p): 
    "ESCAPED : ESC_CRETURN"
    p[0]=p[1]
    

def p_ESCAPED7(p): 
    "ESCAPED : ESC_TAB"
    p[0]="\t"
    

def p_ESCAPED8(p): 
    "ESCAPED : ESC_HEX4"
    p[0]=str(chr(int(p[1].split("\\u")[1], 16)))
    
    
def p_ESCAPED9(p): 
    "ESCAPED : ESC_HEX8"
    p[0]=str(chr(int(p[1].split("\\u")[1], 32)))
    

def p_MULTILINEBASICSTRING(p):
    "MULTILINEBASICSTRING : TRIPLEASPA MLNL MLBASICBODY TRIPLEASPA"
    p[0]=p[3]

def p_MLNL1(p):
    "MLNL : NEWLINE"
    p[0]="\n"

def p_MLNL2(p):
    "MLNL :"
    p[0]=""
    
def p_MLBASICBODY(p):
    "MLBASICBODY : MLBC"
    p[0] = p[1]

def p_MLBC1(p): 
    "MLBC : CONTENTQUOTE MLBC"
    p[0] = p[1] + p[2]

def p_MLBC2(p):
    "MLBC :"
    p[0]=""

def p_CONTENTQUOTE1(p):
    "CONTENTQUOTE : MLBCONTENT"
    p[0] = p[1]

def p_CONTENTQUOTE2(p):
    "CONTENTQUOTE : MLBQUOTES"
    p[0] = p[1]

def p_MLBCONTENT1(p): 
    "MLBCONTENT : MLBCHAR"
    p[0]=p[1]

def p_MLBCONTENT2(p): 
    "MLBCONTENT : NEWLINE"
    p[0]="\n"

def p_MLBCONTENT3(p): 
    "MLBCONTENT : MLBESCAPEDNL"
    p[0] = p[1]

def p_MLBCONTENT4(p): 
    "MLBCONTENT : TWODOT_SEP"
    p[0] = p[1]

def p_MLBCONTENT5(p): 
    "MLBCONTENT : DOT_SEP"
    p[0] = p[1]

def p_MLBCONTENT6(p): 
    "MLBCONTENT : VIRGULA"
    p[0] = p[1]

def p_MLBCHAR1(p): 
    "MLBCHAR : MLBUNESCAPED"
    p[0] = p[1]

def p_MLBCHAR2(p):
    "MLBCHAR : ESCAPED"
    p[0]=p[1]

def p_MLBQUOTES1(p):
    "MLBQUOTES : ASPA"
    p[0] = p[1]

def p_MLBQUOTES2(p):
    "MLBQUOTES : DOUBLEASPA"
    p[0] = p[1]

def p_MLBQUOTES3(p):
    "MLBQUOTES :"
    p[0] =""

def p_MLBUNESCAPED1(p):
    "MLBUNESCAPED : WHITESPACE"
    p[0] = p[1]

def p_MLBUNESCAPED2(p):
    "MLBUNESCAPED : CHAR"
    p[0]=p[1]

def p_MLBESCAPEDNL(p):
    "MLBESCAPEDNL : ESCAPE NEWLINE WHNL"
    p[0] = ""
    

def p_WHNL1(p):
    "WHNL : SPACENEWLINE WHNL"
    p[0] = p[1] + p[2]

def p_WHNL2(p):
    "WHNL :" 
    p[0]=""

def p_SPACENEWLINE1(p):
    "SPACENEWLINE : WHITESPACE"
    p[0] = p[1] 
    
def p_SPACENEWLINE2(p):
    "SPACENEWLINE : NEWLINE"     
    p[0] = p[1] 

def p_LITERALSTRING(p):
    "LITERALSTRING : APOSTROFE LCH APOSTROFE"
    p[0] = p[2]
    

def p_LCH1(p):
    "LCH : LITERALCHAR LCH"
    p[0] = p[1] + p[2] 

def p_LCH2(p):
    "LCH :"
    p[0]=""
    
def p_LITERALCHAR1(p):
    "LITERALCHAR : CHAR"
    p[0] = p[1]

def p_LITERALCHAR2(p):
    "LITERALCHAR : ESCAPED"
    p[0] = p[1]

def p_LITERALCHAR3(p):
    "LITERALCHAR : WHITESPACE"
    p[0] = p[1]

def p_LITERALCHAR4(p):
    "LITERALCHAR : TWODOT_SEP"
    p[0] = p[1]

def p_LITERALCHAR5(p):
    "LITERALCHAR : ASPA"
    p[0] = p[1]

def p_LITERALCHAR6(p):
    "LITERALCHAR : ESCAPE"
    p[0] = p[1]

def p_MLLITERALSTRING(p):
    "MLLITERALSTRING : TRIPLEAPOSTROFE NLR MLLITERALBODY TRIPLEAPOSTROFE"
    p[0] = p[3]    

def p_NLR1(p):
    "NLR : NEWLINE"
    p[0]=""

def p_NLR2(p):
    "NLR :"
    p[0]=""
  
def p_MLLITERALBODY(p):
    "MLLITERALBODY : MLLC"
    p[0] = p[1]

def p_MLLC1(p): 
    "MLLC : MLLCONTENTQUOTES MLLC"
    p[0] = p[1] + p[2]
    
def p_MLLCONTENTQUOTES1(p):
    "MLLCONTENTQUOTES : MLLCONTENT"
    p[0] = p[1]

def p_MLLCONTENTQUOTES2(p):
    "MLLCONTENTQUOTES : MLLQUOTES"
    p[0] = p[1]

def p_MLLC2(p): 
    "MLLC :"
    p[0]=""

def p_MLLCONTENT1(p): 
    "MLLCONTENT : MLLCHAR"
    p[0] = p[1]  

def p_MLLCONTENT2(p): 
    "MLLCONTENT : NEWLINE"
    p[0] = p[1]

def p_MLLCHAR1(p): 
    "MLLCHAR : CHAR"
    p[0] = p[1]

def p_MLLCHAR2(p): 
    "MLLCHAR : DOT_SEP"
    p[0] = p[1]

def p_MLLCHAR3(p): 
    "MLLCHAR : WHITESPACE"
    p[0] = p[1]

def p_MLLCHAR4(p): 
    "MLLCHAR : VIRGULA"
    p[0] = p[1]

def p_MLLQUOTES1(p): 
    "MLLQUOTES : DOUBLEAPOSTROFE"
    p[0] = p[1]
    
def p_MLLQUOTES2(p): 
    "MLLQUOTES : APOSTROFE"
    p[0] = p[1]

def p_MLLQUOTES3(p): 
    "MLLQUOTES : ASPA"
    p[0] = p[1]

def p_MLLQUOTES3(p): 
    "MLLQUOTES :"
    p[0]=""

def p_ARRAY(p):
    "ARRAY : APR ARRAYVALUES WSCOMMENTNEWLINE FPR"
    p[0] = p[2]

def p_ARRAYVALUES1(p):
    "ARRAYVALUES :"
    pass

def p_ARRAYVALUES2(p):
    "ARRAYVALUES : WSCOMMENTNEWLINE VALUE WSCOMMENTNEWLINE ARRAYCONTEUDO"
    p[0] = [p[2]]
    if p[4]:
        p[0].extend(p[4])
        
def p_ARRAYVALUES3(p):
    "ARRAYCONTEUDO :"
    pass
    
def p_ARRAYVALUES4(p):
    "ARRAYCONTEUDO : WSCOMMENTNEWLINE VIRGULA ARRAYVALUES"
    p[0] = p[3]

def p_WSCOMMENTNEWLINE1(p):
    "WSCOMMENTNEWLINE :"
    pass
    

def p_WSCOMMENTNEWLINE2(p):
    "WSCOMMENTNEWLINE : INNERCOMMENT WSCOMMENTNEWLINE"

def p_INNERCOMMENT1(p):
    "INNERCOMMENT : WHITESPACE"

def p_INNERCOMMENT2(p):
    "INNERCOMMENT : COMMENTOUNAO NEWLINE"
    
def p_INNERCOMMENT3(p):
    "INNERCOMMENT : NEWLINE"

def p_COMMENTOUNAO1(p):
    "COMMENTOUNAO : COMMENT"
    

def p_COMMENTOUNAO2(p):
    "COMMENTOUNAO :"
    
def p_TABLE1(p):
    "TABLE : STDTABLE"
    p[0] = p[1]

def p_TABLE2(p):
    "TABLE : TABLEARRAY"
    p[0] = p[1]

def p_STDTABLE(p):
    "STDTABLE : APR KEY FPR"
    if(type(p[2]) is str):
        p[0] = {p[2]:{None}}
    else:p[0] = p[2]    



def p_INLINETABLE(p):
    '''INLINETABLE : ACH FCH'''
    p[0] = {}

def p_INLINETABLE2(p):
    '''INLINETABLE : ACH INLINETABLEWS INLINEKVALUE INLINETABLEWS FCH'''
    p[0] = p[3]
    
def p_INLINETABLEWS1(p):
    '''INLINETABLEWS : '''

def p_INLINETABLEWS2(p):
    '''INLINETABLEWS : WHITESPACE'''

def p_INLINEKVALUE(p):
    '''INLINEKVALUE : INLINEKVALUE INLINETABLEWS VIRGULA INLINETABLEWS KVALUE'''
    converter.fusion(p[1],p[5])
    p[0] = p[1]


def p_INLINEKVALUE2(p):
    '''INLINEKVALUE : KVALUE'''
    p[0] = p[1]

def p_TABLEARRAY1(p):
    '''TABLEARRAY : ATO KEY ATC'''
    if(type(p[2]) is str):
        p[0] = {p[2]:[]}
    else:
        converter.insertLast(p[2],[])
        p[0]=p[2]

def p_error(p):
    print(f"Sintaxe incorreta "+str(p))

parser = yacc.yacc()