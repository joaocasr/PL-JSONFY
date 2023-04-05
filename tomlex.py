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
    'TEMPO',
    'VAR_NAME',
    'ENTRY'
]

t_COMENTARIO= r'\#.+'
t_PALAVRA=r'\".+\"'
t_TEMPO=r'\d+:\d+:\d+'
t_DATE=r'\d+-\d+-\d+'
t_NUMERO=r'\d+'
t_ENTRY=r'\[(:?[a-zA-Z]\w+(:?\.[a-zA-Z]\w+)?)\]' 
t_BOOLEAN = r'(true|false)'
t_APR=r'\['    
t_FPR=r'\]'
t_VIRGULA=r','
t_IGUAL=r'='
t_VAR_NAME=r'[a-zA-Z]\w+'


t_ignore = ' \t\n'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

####################################
# Regras de atribuição
####################################
def p_atrib(p):
    '''atrib : VAR_NAME IGUAL element'''
    p[0] = p[1] + p[2] + p[3]
    print("Atribuição:"+p[0])

def p_element_num(p):
    '''element : NUMERO '''
    p[0] = str(p[1])

def p_element_palavra(p):
    '''element : PALAVRA '''
    p[0] = p[1]

def p_element_bool(p):
    '''element : BOOLEAN'''
    p[0] = p[1]

def p_element_data(p):
    '''element : DATE'''
    p[0] = p[1]

def p_element_tempo(p):
    '''element : TEMPO'''
    p[0] = p[1]

####################################


def p_error(p):
    if p:
        print(f"Error in {p}")
    else:
        print("Error")

parser = yacc.yacc()

