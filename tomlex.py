import ply.lex as lex
import ply.yacc as yacc
import re

tokens = [
    'COMMENT',
    'WHITESPACE',
    'NEWLINE',
    'DOT_SEP',
    'UNDERSCORE',
    'ASPA',
    'UNDERSC0RE',
    'MINUS',
    'PLUS',
    'APOSTROFE',
    'ESC_REVERSE',
    'ESC_BACKSPACE',
    'ESC_QUOTE',
    'ESC_FF',
    'ESC_NL',
    'ESC_CRETURN',
    'ESC_TAB', 
    'ESC_HEX4',
    'ESC_HEX8',
    'APR',
    'FPR',
    'ACH',
    'FCH',
    'VIRGULA',
    'CHAR',
    'ESCAPE',
    'BOOLEAN',
    'INTEGER',
    'FLOAT',
    'INF',
    'NAN',
    'HEX',
    'OCT',
    'BIN',
    'IGUAL',
    'DATE_FULLYEAR',
    'DATE_MONTH',
    'DATE_MDAY',
    'TIME_DELIM',
    'TIME_HOUR',
    'TIME_MIN',
    'TIME_SEC',
    'TIME_SECFRAC',
    'ATO',
    'ATC'
]

# análise léxica
def t_COMMENT(t):r'\#.+';return t
def t_WHITESPACE(t):r'[^\S\t\r\n]';return t
def t_NEWLINE(t):r'\n';return t
def t_DOT_SEP(t):r'\.';return t
def t_UNDERSCORE(t):r'_';return t
def t_IGUAL(t):r'=';return t
def t_ASPA(t):r'\"';return t
def t_APOSTROFE(t):r'\'';return t
def t_ESC_REVERSE(t):r'\\\\';return t
def t_ESC_BACKSPACE(t):r'\\b';return t
def t_ESC_QUOTE(t):r'\\\"';return t
def t_ESC_FF(t):r'\\f';return t
def t_ESC_NL(t):r'\\n';return t
def t_ESC_CRETURN(t):r'\\r';return t
def t_ESC_TAB(t):r'\\t';return t
def t_ESC_HEX4(t):r'\\u([0-9]|[a-fA-F]){4}';return t
def t_ESC_HEX8(t):r'\\u([0-9]|[a-fA-F]){8}';return t
def t_CHAR(t):r'[a-zA-Z]';return t
def t_ESCAPE(t): r'\\';return t
def t_FLOAT(t):r'(?:\+|-)?\d(?:_\d|\d)*\.(?:\d(?:_\d|\d)*)?(?:[eE](?:\+|-)?\d(?:_\d|\d)*)?';return t #a expressao regular estava a apanhar integers (continua com limitacoes)
def t_MINUS(t):r'-';return t
def t_PLUS(t):r'\+';return t
def t_UNDERSC0RE(t):r'_';return t
def t_INTEGER(t):r'(?:\+|-)?\d(?:(?:_\d)|\d)*';return t
def t_HEX(t):r'0x[\da-fA-F](?:(?:_[\da-fA-F])|[\da-fA-F])*';return t
def t_OCT(t):r'0o[0-7](?:(?:_[0-7])|[0-7])*';return t
def t_BIN(t):r'0b[01](?:(?:_[01])|[01])*';return t
def t_INF(t):r'(?:\+|-)?inf';return t
def t_NAN(t):r'(?:\+|-)?nan';return t
def t_BOOLEAN(t): r'(true|false)';return t

def t_DATE_FULLYEAR(t):r'\d{4}';return t
def t_DATE_MONTH(t):r'(1[0-2]|0\d)';return t
def t_DATE_MDAY(t):r'[0-3]\d';return t
def t_TIME_DELIM(t):r'[Tt ]';return t
def t_TIME_HOUR(t):r'[0-2]\d';return t
def t_TIME_MIN(t):r'[0-5]\d';return t
def t_TIME_SEC(t):r'[0-6]\d';return t
def t_TIME_SECFRAC(t):r'.\d+';return t

def t_APR(t):r'\[';return t
def t_FPR(t):r'\]';return t
def t_VIRGULA(t):r',';return t

def t_ACH(t):r'\{';return t
def t_FCH(t):r'\}';return t

def t_ATO(t):r'\[\[';return t
def t_ATC(t):r'\]\]';return t

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

#análise sintática
def p_TOML(p):
    "TOML : EXPRESSION TOML2"
    p[0] = f"""{p[1]}{p[2]}"""

def p_TOML2(p): 
    "TOML2 : NEWLINE EXPRESSION TOML2"
    p[0] = f"""{p[1]}{p[2]}{p[3]}"""

def p_TOML3(p):
    "TOML2 :"
    p[0] = ""

def p_EXPRESSION2(p):
    "EXPRESSION : KVALUE EXPRESSION2"
    p[0] = f"""{p[1]}{p[2]}"""

def p_EXPRESSION1(p):
    "EXPRESSION : EXPRESSION2"
    p[0] = f"""{p[1]}"""

def p_EXPRESSION3(p):
    "EXPRESSION : TABLE EXPRESSION2"
    p[0] = f"""{p[1]}{p[2]}"""

def p_EXPRESSION2_2(p):
    "EXPRESSION2 :"
    p[0] = ""

def p_EXPRESSION2_1(p):
    "EXPRESSION2 : COMMENT"
    p[0] = f"""{p[1]}"""

def p_KVALUE(p):
    "KVALUE : KEY kvwhitespace IGUAL kvwhitespace VALUE"
    p[0] = f"""{p[1]}{p[2]}{p[3]}{p[4]}{p[5]}"""

def p_kvwhitespace1(p):
    "kvwhitespace : WHITESPACE"
    p[0] = f"""{p[1]}"""

def p_kvwhitespace2(p):
    "kvwhitespace :"
    p[0] = ""

def p_KEY1(p):
    "KEY : SIMPLEKEY"
    p[0] = f"""{p[1]}"""

def p_KEY2(p):
    "KEY : DOTKEY"
    p[0] = f"""{p[1]}"""

def p_SIMPLEKEY1(p):
    "SIMPLEKEY : QUOTEDKEY"
    p[0] = f"""{p[1]}"""

def p_SIMPLEKEY2(p):
    "SIMPLEKEY : UNQUOTEDKEY"
    p[0] = f"""{p[1]}"""

def p_UNQUOTEDKEY1(p):
    "UNQUOTEDKEY : OCCURRENCES UNQUOTEDKEYAUX"
    p[0] = f"""{p[1]}{p[2]}"""

def p_UNQUOTEDKEY2(p):
    "UNQUOTEDKEYAUX : OCCURRENCES UNQUOTEDKEYAUX"
    p[0] = f"""{p[1]}{p[2]}"""

def p_UNQUOTEDKEY3(p):
    "UNQUOTEDKEYAUX :"
    p[0] = ""

def p_OCCURRENCES1(p):
    "OCCURRENCES : CHAR"
    p[0] = f"""{p[1]}"""

def p_OCCURRENCES2(p):
    "OCCURRENCES : INTEGER"
    p[0] = f"""{p[1]}"""

def p_OCCURRENCES3(p):
    "OCCURRENCES : MINUS"
    p[0] = f"""{p[1]}"""

def p_OCCURRENCES4(p):
    "OCCURRENCES : UNDERSCORE"
    p[0] = f"""{p[1]}"""

def p_QUOTEDKEY1(p):
    "QUOTEDKEY : BASICSTRING"
    p[0] = f"""{p[1]}"""

def p_QUOTEDKEY2(p):
    "QUOTEDKEY : LITERALSTRING"
    p[0] = f"""{p[1]}"""

def p_DOTKEY(p):
    "DOTKEY : SIMPLEKEY DOT_SEP SIMPLEKEY DOTSIMPKEY"
    p[0] = f"""{p[1]}{p[2]}{p[3]}{p[4]}"""

def p_DOTSIMPKEY1(p): 
    "DOTSIMPKEY : DOT_SEP SIMPLEKEY DOTSIMPKEY"
    p[0] = f"""{p[1]}{p[2]}{p[3]}"""

def p_DOTSIMPKEY2(p):
    "DOTSIMPKEY : "
    p[0] = ""

def p_VALUE1(p):
    "VALUE : STRING"
    p[0] = f"""{p[1]}"""

def p_VALUE2(p):
    "VALUE : BOOLEAN"
    p[0] = f"""{p[1]}"""

def p_VALUE3(p):
    "VALUE : INTEGER"
    p[0] = f"""{p[1]}"""

def p_VALUE4(p):
    "VALUE : ARRAY"
    p[0] = f"""{p[1]}"""

#def p_VALUE5(p):
#    "VALUE : INLINETABLE"
#    p[0] = f"""{p[1]}"""

#def p_VALUE6(p):
#    "VALUE : DATETIME"
#    p[0] = f"""{p[1]}"""

def p_VALUE7(p):
    "VALUE : FLOAT"
    p[0] = f"""{p[1]}"""

def p_STRING1(p) : 
    "STRING : MULTILINEBASICSTRING"
    p[0] = f"""{p[1]}"""

def p_STRING2(p) : 
    "STRING : BASICSTRING"
    p[0] = f"""{p[1]}"""

def p_STRING3(p) : 
    "STRING : MLLITERALSTRING"
    p[0] = f"""{p[1]}"""

def p_STRING4(p) : 
    "STRING : LITERALSTRING"
    p[0] = f"""{p[1]}"""

def p_BASICSTRING1(p):
    "BASICSTRING : ASPA BC ASPA"
    p[0] = f"""{p[1]}{p[2]}{p[3]}"""

def p_BASICSTRING2(p):
    "BC : BASICCHAR BC"
    p[0] = f"""{p[1]}{p[2]}"""

def p_BASICSTRING3(p):
    "BC : "
    p[0] = ""

def p_BASICCHAR1(p):
    "BASICCHAR : BASICUNESCAPED"
    p[0] = f"""{p[1]}"""

def p_BASICCHAR2(p):
    "BASICCHAR : ESCAPED"
    p[0] = f"""{p[1]}"""

def p_BASICUNESCAPED1(p):
    "BASICUNESCAPED : WHITESPACE"
    p[0] = f"""{p[1]}"""

def p_BASICUNESCAPED2(p):
    "BASICUNESCAPED : CHAR"
    p[0] = f"""{p[1]}"""

def p_BASICUNESCAPED3(p):
    "BASICUNESCAPED : INTEGER"
    p[0] = f"""{p[1]}"""

def p_BASICUNESCAPED4(p):
    "BASICUNESCAPED : MINUS"
    p[0] = f"""{p[1]}"""

def p_BASICUNESCAPED5(p):
    "BASICUNESCAPED : APOSTROFE"
    p[0] = f"""{p[1]}"""

def p_BASICUNESCAPED6(p):
    "BASICUNESCAPED : ESCAPED"
    p[0] = f"""{p[1]}"""

def p_BASICUNESCAPED7(p):
    "BASICUNESCAPED : DOT_SEP"
    p[0] = f"""{p[1]}"""

################################
def p_ESCAPED1(p): 
    "ESCAPED : ESC_QUOTE"
    p[0] = f"""{p[1]}"""

def p_ESCAPED2(p): 
    "ESCAPED : ESC_REVERSE"
    p[0] = f"""{p[1]}"""

def p_ESCAPED3(p): 
    "ESCAPED : ESC_BACKSPACE"
    p[0] = f"""{p[1]}"""

def p_ESCAPED4(p): 
    "ESCAPED : ESC_FF"
    p[0] = f"""{p[1]}"""

def p_ESCAPED5(p): 
    "ESCAPED : ESC_NL"
    p[0] = f"""{p[1]}"""

def p_ESCAPED6(p): 
    "ESCAPED : ESC_CRETURN"
    p[0] = f"""{p[1]}"""

def p_ESCAPED7(p): 
    "ESCAPED : ESC_TAB"
    p[0] = f"""{p[1]}"""

def p_ESCAPED8(p): 
    "ESCAPED : ESC_HEX4"
    #print(chr(int(p[1].split("\\u")[1], 16)))
    p[1]=chr(int(p[1].split("\\u")[1], 16))
    p[0] = f"""{p[1]}"""
    
def p_ESCAPED9(p): 
    "ESCAPED : ESC_HEX8"
    #print(chr(int(p[1].split("\\u")[1], 32)))
    p[1]=chr(int(p[1].split("\\u")[1], 32))
    p[0] = f"""{p[1]}"""

def p_MULTILINEBASICSTRING(p):
    "MULTILINEBASICSTRING : MLBCSTRDELIM MLNL MLBASICBODY MLBCSTRDELIM"
    p[0] = f"""{p[1]}{p[2]}{p[3]}{p[4]}"""

def p_MLNL(p):
    "MLNL : NEWLINE"
    p[0] = f"""{p[1]}"""

def p_MLBCSTRDELIM(p):
    "MLBCSTRDELIM : ASPA ASPA ASPA"
    p[0] = f"""{p[1]}{p[2]}{p[3]}"""

def p_MLBASICBODY(p):
    "MLBASICBODY : MLBC MLBQC MLQ"
    p[0] = f"""{p[1]}{p[2]}{p[3]}"""

def p_MLBC1(p): 
    "MLBC : MLBCONTENT MLBC"
    p[0] = f"""{p[1]}{p[2]}"""

def p_MLBC2(p):
    "MLBC : "
    p[0] = ""

def p_MLBQC1(p): 
    "MLBQC : MLBQUOTES MLBCONTENT MLBC2 MLBQC"
    p[0] = f"""{p[1]}{p[2]}{p[3]}{p[4]}"""

def p_MLBQC2(p):
    "MLBQC : "
    p[0] = ""

def p_MLBC2_1(p): 
    "MLBC2 : MLBCONTENT MLBC2"
    p[0] = f"""{p[1]}{p[2]}"""

def p_MLBC2_2(p):
    "MLBC2 : "
    p[0] = ""

def p_MLQ1(p): 
    "MLQ : MLBQUOTES" 
    p[0] = f"""{p[1]}"""

def p_MLQ2(p):
    "MLQ : "
    p[0] = ""

def p_MLBCONTENT1(p): 
    "MLBCONTENT : MLBCHAR"
    p[0] = f"""{p[1]}"""

def p_MLBCONTENT2(p): 
    "MLBCONTENT : NEWLINE"
    p[0] = f"""{p[1]}"""

def p_MLBCONTENT3(p): 
    "MLBCONTENT : MLBESCAPEDNL"
    p[0] = f"""{p[1]}"""

def p_MLBCHAR1(p): 
    "MLBCHAR : MLBUNESCAPED"
    p[0] = f"""{p[1]}"""

def p_MLBCHAR2(p):
    "MLBCHAR : ESCAPED"
    p[0] = f"""{p[1]}"""

def p_MLBQUOTES1(p):
    "MLBQUOTES : ASPA"
    p[0] = f"""{p[1]}"""

def p_MLBQUOTES2(p): 
    "MLBQUOTES : ASPA ASPA"
    p[0] = f"""{p[1]}{p[2]}"""

def p_MLBUNESCAPED1(p):
    "MLBUNESCAPED : WHITESPACE"
    p[0] = f"""{p[1]}"""

def p_MLBUNESCAPED2(p):
    "MLBUNESCAPED : CHAR"
    p[0] = f"""{p[1]}"""

def p_MLBESCAPEDNL(p):
    "MLBESCAPEDNL : ESCAPE WHITESPACE NEWLINE WHNL"
    p[0] = f"""{p[1]}{p[2]}{p[3]}{p[4]}"""

def p_WHNL1(p):
    "WHNL : SPACENEWLINE WHNL"
    p[0] = f"""{p[1]}{p[2]}"""

def p_WHNL2(p):
    "WHNL : " 
    p[0] = ""

def p_SPACENEWLINE1(p):
    "SPACENEWLINE : WHITESPACE" 
    p[0] = f"""{p[1]}"""

def p_SPACENEWLINE2(p):
    "SPACENEWLINE : NEWLINE"     
    p[0] = f"""{p[1]}"""

def p_LITERALSTRING(p):
    "LITERALSTRING : APOSTROFE LCH APOSTROFE"
    p[0] = f"""{p[1]}{p[2]}{p[3]}"""

def p_LCH1(p):
    "LCH : LITERALCHAR LCH"
    p[0] = f"""{p[1]}{p[2]}"""

def p_LCH2(p):
    "LCH : "
    p[0] = ""

def p_LITERALCHAR1(p):
    "LITERALCHAR : CHAR"
    p[0] = f"""{p[1]}"""

def p_LITERALCHAR2(p):
    "LITERALCHAR : ESCAPED"
    p[0] = f"""{p[1]}"""

def p_MLLITERALSTRING(p):
    "MLLITERALSTRING : MLLITERALSTRINGDELIM NLR MLLITERALBODY NLR MLLITERALSTRINGDELIM"
    p[0] = f"""{p[1]}{p[2]}{p[3]}{p[4]}{p[5]}"""

def p_NLR1(p):
    "NLR : NEWLINE"
    p[0] = f"""{p[1]}"""

def p_NLR2(p):
    "NLR :"
    p[0] = ""

def p_MLLITERALSTRINGDELIM(p):
    "MLLITERALSTRINGDELIM : APOSTROFE APOSTROFE APOSTROFE"
    p[0] = f"""{p[1]}{p[2]}{p[3]}"""

#def p_MLLITERALBODY1(p):
#    "MLLITERALBODY : MLLC"
#    p[0] = f"""{p[1]}"""

def p_MLLITERALBODY(p):
    "MLLITERALBODY : MLLC MLLQC MLLQ"
    p[0] = f"""{p[1]}{p[2]}{p[3]}"""

def p_MLLC1(p): 
    "MLLC : MLLCONTENT MLLC"
    print(p[1])
    p[0] = f"""{p[1]}{p[2]}"""

def p_MLLC2(p): 
    "MLLC :"
    p[0] = ""

def p_MLLQC1(p): 
    "MLLQC :"
    p[0] = ""

def p_MLLQC2(p): 
    "MLLQC : MLLQUOTES MLLCONTENT MLLC2 MLLQC"
    p[0] = f"""{p[1]}{p[2]}{p[3]}{p[4]}"""

def p_MLLC2_1(p): 
    "MLLC2 : MLLCONTENT MLLC2"
    p[0] = f"""{p[1]}{p[2]}"""

def p_MLLC2_2(p): 
    "MLLC2 : "
    p[0] = ""

def p_MLLQ1(p): 
    "MLLQ :"
    p[0] = ""

def p_MLLQ2(p): 
    "MLLQ : MLLQUOTES"
    p[0] = f"""{p[1]}"""

def p_MLLCONTENT1(p): 
    "MLLCONTENT : MLLCHAR"
    p[0] = f"""{p[1]}"""

def p_MLLCONTENT2(p): 
    "MLLCONTENT : NEWLINE"
    p[0] = f"""{p[1]}"""

def p_MLLCHAR(p): 
    "MLLCHAR : CHAR"
    p[0] = f"""{p[1]}"""

def p_MLLQUOTES1(p): 
    "MLLQUOTES : APOSTROFE APOSTROFE"
    p[0] = f"""{p[1]}{p[2]}"""

def p_MLLQUOTES2(p): 
    "MLLQUOTES : APOSTROFE"
    p[0] = f"""{p[1]}"""

def p_ARRAY(p):
    "ARRAY : APR ARRAYVALUES WSCOMMENTNEWLINE FPR"
    p[0] = f"""{p[1]}{p[2]}{p[3]}{p[4]}"""

def p_ARRAYVALUES1(p):
    "ARRAYVALUES :"
    p[0] = ""

def p_ARRAYVALUES2(p):
    "ARRAYVALUES : WSCOMMENTNEWLINE VALUE ARRAYCONTEUDO"
    p[0] = f"""{p[1]}{p[2]}{p[3]}"""

def p_ARRAYVALUES3(p):
    "ARRAYCONTEUDO :"
    p[0] = ""

def p_ARRAYVALUES4(p):
    "ARRAYCONTEUDO : WSCOMMENTNEWLINE VIRGULA ARRAYVALUES"
    p[0] = f"""{p[1]}{p[2]}{p[3]}"""

#def p_ARRAYVALUES3(p):
#    "ARRAYVALUES : WSCOMMENTNEWLINE VALUE WSCOMMENTNEWLINE SEPARATOR"
#    p[0] = f"""{p[1]}{p[2]}{p[3]}{p[4]}"""

#def p_SEPARATOR(p):
#    "SEPARATOR :"
#    p[0] = ""

#def p_SEPARATOR(p):
#    "SEPARATOR : VIRGULA"
#    p[0] = f"""{p[1]}"""

def p_WSCOMMENTNEWLINE1(p):
    "WSCOMMENTNEWLINE :"
    p[0] = ""

def p_WSCOMMENTNEWLINE2(p):
    "WSCOMMENTNEWLINE : INNERCOMMENT WSCOMMENTNEWLINE"
    p[0] = f"""{p[1]}{p[2]}"""

def p_INNERCOMMENT1(p):
    "INNERCOMMENT : WHITESPACE"
    p[0] = f"""{p[1]}"""

def p_INNERCOMMENT2(p):
    "INNERCOMMENT : COMMENTOUNAO NEWLINE"
    p[0] = f"""{p[1]}{p[2]}"""

def p_COMMENTOUNAO1(p):
    "COMMENTOUNAO : COMMENT"
    p[0] = f"""{p[1]}"""

def p_COMMENTOUNAO2(p):
    "COMMENTOUNAO :"
    p[0] = ""

def p_TABLE(p):
    "TABLE : APR KEY FPR"
    p[0] = f"""{p[1]}{p[2]}{p[3]}"""


def p_error(p):
    print(f"Sintaxe incorreta "+str(p))


parser = yacc.yacc()
