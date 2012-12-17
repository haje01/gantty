#!/usr/bin/env python
# encoding=utf-8

import ply

tokens = (
    'NAME', 'NUMBER', '4DIGIT', '2DIGIT',
    'LPAREN', 'RPAREN', 'AT', 'SLASH', 'PERCENT', 'ARROW', 'WEEK', 'DAY',
    'HOUR',
)

# Tokens
t_LPAREN = r'\['
t_RPAREN = r'\]'
t_AT = r'@'
t_SLASH = r'/'
t_PERCENT = r'%'
t_WEEK = r'w'
t_DAY = r'd'
t_HOUR = r'h'
t_ARROW = r'->'
t_NAME = r'[^\[\]]+'
t_4DIGIT = r'\d{4}'
t_2DIGIT = r'\d{2}'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print ("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lex.lex()

def p_task(p):
    'task : LPAREN NAME RPAREN due'
    names[p[2]] = p[4]

def p_due(p):
    '''due : NUMBER WEEK 
                | NUMBER DAY 
                | NUMBER HOUR'''
    p[0] = p[1]

def p_taskbody_date(p):
    'taskbody : 4DIGIT SLASH 2DIGIT SLASH 2DIGIT'
    p[0] = p[1]

def p_error(p):
    if p:
        print ("Syntax error at '%s'" % p.value)
    else:
        print ('Syntax error')

import ply.yacc as yacc
yacc.yacc()

s  = raw_input('>')
r = yacc.parse(s)
if r:
    print r

