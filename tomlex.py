import ply.lex as lex
import ply.yacc as yacc
import re

tokens = [
    'COMMENT',
    'WHITESPACE',
    'NEWLINE',
    'DOT_SEP',
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
t_COMMENT=r'\#.+'
t_WHITESPACE=r'[^\S\t\r\n]'
t_NEWLINE=r'\n'
t_DOT_SEP=r'\.'
t_IGUAL=r'='
t_ASPA=r'\"'
t_APOSTROFE=r'\''
t_ESC_REVERSE=r'\\\\'
t_ESC_BACKSPACE=r'\\b'
t_ESC_QUOTE=r'\\\"'
t_ESC_FF=r'\\f'
t_ESC_NL=r'\\n'
t_ESC_CRETURN=r'\\r'
t_ESC_TAB=r'\\t'
t_ESC_HEX4=r'\\u([0-9]|[a-fA-F]){4}'
t_ESC_HEX8=r'\\u([0-9]|[a-fA-F]){8}'
t_CHAR=r'[a-zA-Z]'

t_MINUS=r'-'
t_PLUS=r'\+'
t_UNDERSC0RE=r'_'
t_INTEGER=r'(?:\+|-)?\d(?:(?:_\d)|\d)*'
t_HEX=r'0x[\da-fA-F](?:(?:_[\da-fA-F])|[\da-fA-F])*'
t_OCT=r'0o[0-7](?:(?:_[0-7])|[0-7])*'
t_BIN=r'0b[01](?:(?:_[01])|[01])*'
t_FLOAT=r'(?:\+|-)?\d(?:_\d|\d)*(?:\.\d(?:_\d|\d)*)?(?:[eE](?:\+|-)?\d(?:_\d|\d)*)?'
t_INF=r'(?:\+|-)?inf'
t_NAN=r'(?:\+|-)?nan'
t_BOOLEAN = r'(true|false)'

t_DATE_FULLYEAR=r'\d{4}'
t_DATE_MONTH=r'(1[0-2]|0\d)'
t_DATE_MDAY=r'[0-3]\d'
t_TIME_DELIM=r'[Tt ]'
t_TIME_HOUR=r'[0-2]\d'
t_TIME_MIN=r'[0-5]\d'
t_TIME_SEC=r'[0-6]\d'
t_TIME_SECFRAC=r'.\d+'

t_APR=r'\['
t_FPR=r'\]'
t_VIRGULA=r','

t_ACH=r'\{'
t_FCH=r'\}'

t_ATO=r'\[\['
t_ATC=r'\]\]'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

#análise sintática
'''
def p_error(p):
    print(f"Sintaxe incorreta "+p)

parser = yacc.yacc()
'''