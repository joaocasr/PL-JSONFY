import ply.lex as lex
import ply.yacc as yacc
import re

tokens = [
    'COMENTARIO',
    'APR',
    'FPR',
    'VIRGULA',
    'PALAVRA',
    'NUMERO',
    'BOOLEAN',
    'IGUAL',
    'DATE',
    'TIME',
    'VAR_NAME',
    'ENTRY'
]

def t_ignone_COMENTARIO(t):
    r'\#.+'
    pass

t_ignore = ' \t\n'

# análise léxica
t_PALAVRA=r'\".+\"'
t_TIME=r'\d+:\d+:\d+'
t_DATE=r'\d+-\d+-\d+'
t_NUMERO=r'\d+'
t_ENTRY=r'\[(:?[a-zA-Z]\w+(:?\.[a-zA-Z]\w+)*)\]' 
t_BOOLEAN = r'(true|false)'
t_APR=r'\['    
t_FPR=r'\]'
t_VIRGULA=r','
t_IGUAL=r'='
t_VAR_NAME=r'[a-zA-Z]\w+'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

#análise sintática
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