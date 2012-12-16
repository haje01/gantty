#!/usr/bin/env python
import ply.lex as lex

tokens = (
    'NUMBER', 
    'SPACE',
    'TAB',
    'SHARP',
    'SLASH',
    'STAR',
    'TERM',
    'PERCENT',
    'LBRAC',
    'RBRAC',
    'PRINTABLE',
)

t_SPACE = r'[ ]+'
t_TAB = r'\t'
t_SHARP = r'\#'
t_PERCENT = r'%'
t_SLASH = r'/'
t_STAR = r'\*'
t_PRINTABLE = r'[\S]+'

def t_LBRAC(t):
    r'\['
    return t

def t_RBRAC(t):
    r'\]'
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

