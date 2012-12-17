#!/usr/bin/env python
import ply.lex as lex

tokens = (
    'TASKNAME',
    'MILESTONENAME',
    'SPACE',
    'TAB',
    'TERM',
    'YEARMONTHDAY',
    'MONTHDAY',
    'DONE',
    'COMMENT',
    'NEWLINE',
)

t_SPACE = r'[ ]+'
t_TAB = r'\t'


def t_TASKNAME(t):
    r'\[[^\]]+\]'
    t.value = t.value.strip('[').rstrip(']').strip()
    return t

def t_MILESTONENAME(t):
    r'\*[^\]]+\*'
    t.value = t.value.strip('*').rstrip('*').strip()
    return t

def t_YEARMONTHDAY(t):
    r'\d{4}/\d{2}/\d{2}'
    return t

def t_MONTHDAY(t):
    r'\d{2}/\d{2}'
    return t

def t_TERM(t):
    r'\d+[whd]'
    return t

def t_DONE(t):
    r'1?\d{0,2}\%'
    return t

def t_COMMENT(t):
    r'\#.*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.type = 'NEWLINE'
    t.value = ''
    return t


def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

lexer = lex.lex()

# Test

data = '''
[task 1] 2012/01/23 2w 10%
    [task 1-1] 02/02 100% # comment 1
	[task 2] 0%
# comment 2
*close beta* 2012/06/06
'''

lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: break
    print tok.type, tok.value, tok.lineno, tok.lexpos

