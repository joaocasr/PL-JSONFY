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
    'DIGIT',
    'BOOLEAN',
    'IGUAL',
    'DATE',
    'TIME',
]

# análise léxica
t_COMMENT=r'\#.+'
t_WHITESPACE=r'[^\S\t\r\n]'
t_NEWLINE=r'\n'
t_DOT_SEP=r'\.'
t_ASPA=r'\"'
t_UNDERSC0RE=r'_'
t_MINUS=r'-'
t_APOSTROFE=r'\''
t_ESC_REVERSE=r'\\\\'
t_ESC_BACKSPACE=r'\\b'
t_ESC_QUOTE=r'\\\"'
t_ESC_FF=r'\\f'
t_ESC_NL=r'\\n'
t_ESC_CRETURN=r'\\r'
t_ESC_TAB=r'\\t'
t_ESC_HEX4=r'\\u([0-9]|[A-F]){4}'
t_ESC_HEX8=r'\\u([0-9]|[A-F]){8}'
t_CHAR=r'[a-zA-Z]'
t_TIME=r'\d+:\d+:\d+'
t_DATE=r'\d+-\d+-\d+'
t_DIGIT=r'\d'
t_BOOLEAN = r'(true|false)'
t_APR=r'\['    
t_FPR=r'\]'
t_ACH=r'\{'    
t_FCH=r'\}'
t_VIRGULA=r','
t_IGUAL=r'='

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