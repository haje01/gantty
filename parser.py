#!/usr/bin/env python
import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'TASKNAME',
    'COMMENT',
    'YEARMONTHDAY',
    'MONTHDAY',
    'INDENT',
    'SPACE',
    'TERM',
    'NEWLINE',
)

t_INDENT = r'^[\s\t]+'
t_SPACE = r'\s+'

tasks = {}
cur_task = None

class Task(object):
    def __init__(self, name):
        object.__init__(self)
        self.name = name

def t_COMMENT(t):
    r'\#.*'

def t_TASKNAME(t):
    r'\[[^\]]+\]'
    t.value = t.value.strip('[').rstrip(']').strip()
    return t

def t_YEARMONTHDAY(t):
    r'\d{4}/\d{2}/\d{2}'
    return t

def t_MONTHDAY(t):
    r'\d{4}/\d{2}/\d{2}'
    return t

def t_TERM(t):
    r'\d[wdh]'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.type = 'NEWLINE'
    return t

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

lexer = lex.lex()

def p_program(p):
    '''program : program statement
               | statement'''

def p_statement(p):
    '''statement : task
                 | NEWLINE'''
    p[0] = p[1]
    print 'statement ', p[0]

def p_task(p):
    '''task : TASKNAME NEWLINE
            | TASKNAME SPACE taskbody NEWLINE'''
    print 'task '

def p_taskbody(p):
    '''taskbody : start
                | start SPACE end'''
    print 'taskbody ', p[0]

def p_start(p):
    '''start : YEARMONTHDAY
             | MONTHDAY'''
    p[0] = p[1]
    print 'start ', p[0]

def p_end(p):
    '''end : YEARMONTHDAY
          | MONTHDAY
          | TERM'''
    p[0] = p[1]
    print 'end ', p[0]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print p
        print "Syntax error at '%s'" % p.value
    else:
        print "Ambiguous syntax error"

parser = yacc.yacc()

# Test

data = '''
[task 1]
[task 2] 2012/01/01
[task 3] 2012/01/01 2012/02/01
[task 4] 2012/01/01 2w
'''

def lex_output():
    print 'Tokenizing..'
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok: break
        print tok.type, tok.value, tok.lineno, tok.lexpos
lex_output()

print 'Parsing..'
parser.parse(data + '\n')
