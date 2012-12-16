#!/usr/bin/env python
import ply.lex as lex

tokens = (
    '4DIGIT',
    '2DIGIT',
    'NUMBER', 
    'TASKNAME',
    'MILESTONENAME',
    'SPACE',
    'TAB',
    'COMMENT',
    'SLASH',
    'TERM',
    'PERCENT',
)

t_SPACE = r'[ ]+'
t_TAB = r'\t'
t_COMMENT = r'\#.*'
t_SLASH = r'/'

def t_TASKNAME(t):
    r'\[([^\]]+)\]'
    t.value = t.value.strip().strip('[').rstrip(']')
    return t

def t_MILESTONENAME(t):
    r'\*([^\*]+)\*'
    t.value = t.value.strip().strip('*').rstrip('*')
    return t

def t_TERM(t):
    r'\d+[whd]'
    return t

def t_PERCENT(t):
    r'1?\d{0,2}%'
    return t

def t_4DIGIT(t):
    r'\d{4}'
    t.value = int(t.value)
    return t

def t_2DIGIT(t):
    r'\d{2}'
    t.value = int(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

lexer = lex.lex()

# Test

data = '''
[task 1] 2012/01/23 2w 10%
    [task 1-1] 100 %# comment 1
	[task 2] 0%
# comment 2
*close beta*
'''

lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: break
    print tok.type, tok.value, tok.lineno, tok.lexpos

