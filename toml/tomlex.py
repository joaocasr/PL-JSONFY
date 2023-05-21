import ply.lex as lex
import re

tokens = [
    'COMMENT',
    'WHITESPACE',
    'NEWLINE',
    'DOT_SEP',
    'TWODOT_SEP',
    'UNDERSCORE',
    'TRIPLEASPA',
    'DOUBLEASPA',
    'ASPA',
    'UNDERSC0RE',
    'MINUS',
    'PLUS',
    'TRIPLEAPOSTROFE',
    'DOUBLEAPOSTROFE',
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
    'DATE',
    'TIME_DELIM',
    'TIME',
    'ATO',
    'ATC'
]

# análise léxica
def t_COMMENT(t):r'\#.+';return t
def t_WHITESPACE(t):r'[^\S\r\n]';return t
def t_NEWLINE(t):r'\n';return t
def t_TWODOT_SEP(t): r':'; return t
def t_UNDERSCORE(t):r'_';return t
def t_IGUAL(t):r'=';return t
def t_TRIPLEASPA(t):r'\"\"\"';return t
def t_DOUBLEASPA(t):r'\"\"';return t
def t_ASPA(t):r'\"';return t
def t_TRIPLEAPOSTROFE(t):r'\'\'\'';return t
def t_DOUBLEAPOSTROFE(t):r'\'\'';return t
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
def t_BOOLEAN(t): r'(true|false)';return t
def t_ESCAPE(t): r'\\';return t
def t_FLOAT(t):r'((?:\+|-)?\d(?:_\d|\d)*\.(?:\d(?:_\d|\d)*)+(?:[eE](?:\+|-)?\d(?:_\d|\d)*)?|(?:\+|-)?\d+(?:[eE](?:\+|-)?\d(?:_\d|\d)*))';return t 

def t_DATE(t):r'\d{4}-(1[0-2]|0\d)-[0-3]\d'; return t
def t_TIME(t):r'[Tt ]?[0-2]\d:[0-5]\d:[0-6]\d(\.\d+)?(Z|(\+|\-)[0-2]\d:[0-5]\d)?'; return t

def t_CHAR(t):r'[a-zA-Z]';return t
def t_MINUS(t):r'-';return t
def t_PLUS(t):r'\+';return t
def t_DOT_SEP(t):r'\.';return t

def t_UNDERSC0RE(t):r'_';return t
def t_INTEGER(t):r'(?:\+|-)?\d(?:(?:_\d)|\d)*';return t
def t_HEX(t):r'0x[\da-fA-F](?:(?:_[\da-fA-F])|[\da-fA-F])*';return t
def t_OCT(t):r'0o[0-7](?:(?:_[0-7])|[0-7])*';return t
def t_BIN(t):r'0b[01](?:(?:_[01])|[01])*';return t
def t_INF(t):r'(?:\+|-)?inf';return t
def t_NAN(t):r'(?:\+|-)?nan';return t

def t_ATO(t):r'\[\[';return t
def t_ATC(t):r'\]\]';return t

def t_APR(t):r'\[';return t
def t_FPR(t):r'\]';return t
def t_VIRGULA(t):r',';return t

def t_ACH(t):r'\{';return t
def t_FCH(t):r'\}';return t


def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

#análise sintática
