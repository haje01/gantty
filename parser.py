#!/usr/bin/env python
import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'TASKNAME',
    'MILESTONENAME',
    'YEARMONTHDAY',
    'MONTHDAY',
    'SPACE',
    'TERM',
    'NEWLINE',
    'PERCENT',
    'PERSON',
    'ARROW',
)

t_SPACE = r'\s+'
t_ARROW = r'<-'
t_ignore_COMMENT = '\#.*'

tasks = {}
cur_task = None

class Task(object):
    def __init__(self, name):
        object.__init__(self)
        self.name = name


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
    r'\d{4}/\d{2}/\d{2}'
    return t

def t_TERM(t):
    r'\d[wdh]'
    return t

def t_PERCENT(t):
    r'1?\d{1,2}%'
    return t

def t_PERSON(t):
    r'@\S+'
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
    '''statement : indent task
                 | indent milestone
                 | SPACE NEWLINE
                 | NEWLINE
                 | SPACE'''
    p[0] = p[1]
    print 'statement ', p[0]

def p_indent(p):
    '''indent : SPACE
              | empty'''
    print 'indent ', p[1:]

def p_task(p):
    '''task : TASKNAME NEWLINE
            | TASKNAME SPACE taskbody NEWLINE'''
    print 'task ', p[1:]

def p_milestone(p):
    '''milestone : MILESTONENAME newline
            | MILESTONENAME SPACE milestonebody newline'''
    print 'milestone ', p[1:]

def p_newline(p):
    '''newline : NEWLINE
               | SPACE NEWLINE'''

def p_taskbody(p):
    '''taskbody : period done person depend'''
    print 'taskbody ', p[0]

def p_milestonebody(p):
    '''milestonebody : start space depend'''
    print 'taskbody ', p[0]

def p_space(p):
    '''space : SPACE
             | empty'''

def p_period(p):
    '''period : start 
              | start SPACE end
              | end
              | empty'''

def p_start(p):
    '''start : SPACE YEARMONTHDAY
             | SPACE MONTHDAY'''
    p[0] = p[1]
    print 'start ', p[0]

def p_end(p):
    '''end : YEARMONTHDAY
          | MONTHDAY
          | TERM'''
    p[0] = p[1]
    print 'end ', p[0]

def p_done(p):
    '''done : SPACE PERCENT
            | empty'''
    p[0] = p[1]
    print 'done ', p[0]

def p_person(p):
    '''person : person SPACE PERSON
              | SPACE PERSON
              | empty'''
    print 'person ', p[1:]

def p_depend(p):
    '''depend : ARROW SPACE TASKNAME
              | ARROW SPACE MILESTONENAME
              | empty'''
    print 'depend ', p[1:]

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
def test():
    data = '''
# comment 1
*start*
[task 1]
[task 2] 2012/01/01
[task 3] 2012/01/01 2012/02/01 # comment 2
[task 4] 2012/01/01 2w
[task 5] 2012/01/01 2w 30%
[task 6] 2012/01/01 2w 100% @haje01
[task 7] 2012/01/01 2w 30% @haje01 @lqez
[task 8] 2012/01/01 2w 30% @haje01 @lqez <- [task 1]
[task 9]
    [task 9-1] 2w 0%
    [task 9-2] 2012/02/15 10% <- [task 9-1]
        [task 9-2-1] 2012/02/17 3d 0% @haje01
*end* 2012/03/01 <- [task 9] # comment 3
    '''

    def lex_output():
        print 'Tokenizing..'
        lexer.input(data)
        while True:
            tok = lexer.token()
            if not tok: break
            print tok.type, tok.value, tok.lineno, tok.lexpos
    lex_output()

    def parse():
        print 'Parsing..'
        parser.parse(data + '\n')
    parse()

if __name__ == '__main__':
    test()

