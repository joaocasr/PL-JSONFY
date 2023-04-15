import ply.lex as lex
import ply.yacc as yacc
import re

tokens = [
    'COMMENT',
    'WHITESPACE',
    'NEWLINE',
    'DOT_SEP',
    'QUOTE',
    'ASPA',
    'UNDERSC0RE',
    'MINUS',
    'APOSTROFE',
    'ESC_REVERSE',
    'ESC_BACKSPACE', 
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
    'MULTILINESTRING',
    'VIRGULA',
    'CHAR',
    'NUMERO',
    'BOOLEAN',
    'IGUAL',
    'DATE',
    'TIME',
]

def t_ignone_COMENTARIO(t):
    r'\#.+'
    pass


# análise léxica
t_MULTILINESTRING=r'\"\"\"(\n?.+)+\n?\"\"\"'
t_WHITESPACE=r'[^\S\t\r\n]'
t_NEWLINE=r'\n'
t_DOT_SEP=r'\.'
t_ASPA=r'\"'
t_UNDERSC0RE=r'_'
t_MINUS=r'-'
t_APOSTROFE=r'\''
t_ESC_REVERSE=r'\\\\'
t_ESC_BACKSPACE=r'\\b'
t_ESC_FF=r'\\f'
t_ESC_NL=r'\\n'
t_ESC_CRETURN=r'\\r'
t_ESC_TAB=r'\\t'
t_ESC_HEX4=r'\\u([0-9]|[A-F]){4}'
t_ESC_HEX8=r'\\u([0-9]|[A-F]){8}'
t_QUOTE=r'\\"'
t_CHAR=r'[a-zA-Z]'
t_TIME=r'\d+:\d+:\d+'
t_DATE=r'\d+-\d+-\d+'
t_NUMERO=r'\d+'
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
def p_TOML(p): "TOML : titulos seccoes"
def p_titulos1(p): "titulos : atribuicao titulos"
def p_titulos2(p): "titulos : "
def p_seccoes1(p): "seccoes : grupo seccoes"
def p_seccoes2(p): "seccoes : "
def p_grupo(p): "grupo : lheaders body"
def p_lheaders1(p): "lheaders : header lheaders"
def p_lheaders2(p): "lheaders : header"
def p_header(p): "header : ENTRY"
def p_body1(p): "body : atribuicao body"
def p_body2(p): "body : atribuicao"
def p_atribuicao(p): "atribuicao : VAR_NAME IGUAL termo"

def p_termo1(p): "termo : PALAVRA"
def p_termo2(p): "termo : NUMERO"
def p_termo3(p): "termo : BOOLEAN"
def p_termo4(p): "termo : DATE"
def p_termo5(p): "termo : TIME"
def p_termo6(p): "termo : lista"

def p_lista(p): "lista : APR conteudo FPR"
def p_conteudo1(p):"conteudo : "
def p_conteudo2(p):"conteudo : termo auxconteudo"
def p_auxconteudo1(p): "auxconteudo : VIRGULA conteudo"
def p_auxconteudo2(p) : "auxconteudo : "


def p_error(p):
    print(f"Sintaxe incorreta "+p)

parser = yacc.yacc()
'''