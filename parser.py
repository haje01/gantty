#!/usr/bin/env python
import ply.yacc as yacc
import lexer

tokens = lexer.tokens

def p_program(p):
    '''program : program statement
               | statement'''
    print 'program ', p[1:]

### all statements

def p_statement(p):
    '''statement : command NEWLINE'''
    if isinstance(p[1], str):
        print 'Error ', p[1]
    else:
        p[0] = p[1]
        print 'statement ', p[1:]

def p_statement_error(p):
    '''statement : error NEWLINE'''
    print "Malformed statement at line %d '%s'" % (p[1].lineno, str(p[1].value))
    p[0] = None
    p.parser.error = 1

def p_statement_blank(p):
    '''statement : NEWLINE'''

### comment
def p_command_comment(p):
    '''command : COMMENT'''
    print 'command comment ', p[1]

### task
def p_command_task(p):
    '''command : TASKNM optstart optend optdone optownerlist optdepend optcomment'''
    print 'command task ', p[1:]

### optional start
def p_optstart(p):
    '''optstart : date
                | empty'''
    p[0] = p[1]
    print 'optstart ', p[1]

### optional end
def p_optend(p):
    '''optend : date
              | empty'''
    p[0] = p[1]
    print 'optend ', p[1]

### optional done
def p_optdone(p):
    '''optdone : PERCENT
               | empty'''
    p[0] = p[1]
    print 'optdone ', p[1]

### optional ownerlist
def p_optownerlist(p):
    '''optownerlist : ownerlist
                    | empty'''
    p[0] = p[1]
    print 'optownerlist ', p[1]

### optional depend
def p_optdepend(p):
    '''optdepend : depend
                    | empty'''
    p[0] = p[1]
    print 'optdepend ', p[1]

def p_depend(p):
    '''depend : ARROW TASKNM'''
    p[0] = p[2]
    print 'depend ', p[1]

### optional comment
def p_optcomment(p):
    '''optcomment : COMMENT
                  | empty'''
    print 'optcomment ', p[1]

### ownerlist
def p_ownerlist(p):
    '''ownerlist : ownerlist OWNER
                 | OWNER'''
    print 'ownerlist ', p[1:]

### date
def p_date(p):
    '''date : YEARMONTHDAY
            | MONTHDAY
            | TERM'''
    p[0] = p[1]
    print 'date ', p[1]

### empty

def p_empty(p):
    '''empty : '''

###  catastrophic error handler
def p_error(p):
    if not p:
        print "Syntax error at EOF"

parser = yacc.yacc()

def parse(data):
    parser.error = 0
    p = parser.parse(data + '\n')
    if parser.error:
        return None
    return p

def test():
    data = '''
# line comment
[task 1]
[task 2] 2012/01/01 @haje01 @lqez # tail comment
[task 3] 2012/01/01 2w 10% @lqez <- [task 2]
'''
    print parse(data)

if __name__ == '__main__':
    test()

