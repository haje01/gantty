#!/usr/bin/env python
import ply.yacc as yacc
import lexer
import types
from objects import Task, Milestone

tokens = lexer.tokens
pindent_char = None
pindent_size = None
pindent_unit = None

def find_column(input, lexpos):
    last_cr = input.rfind('\n', 0, lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (lexpos - last_cr) + 1
    return column

def collect_stmts(target, program):
    if program:
        for stmt in program:
            if type(stmt) == types.ListType:
                collect_stmts(target, stmt)
            elif stmt:
                target.append(stmt)

def check_indent_consistency(indent):
    global pindent_char, pindent_unit, pindent_size

    if len(indent) == 0:
        return

    tab = None
    space = None
    indent_char = None

    if indent.find('\t') >= 0:
        tab = True
        indent_char = '\t'
    if indent.find(' ') >= 0:
        space = True
        indent_char = ' '
    if tab and space:
        return "Space and tab are mixed"

    if not pindent_char:
        pindent_char = indent_char
    elif pindent_char != indent_char:
        return "Different indent character used"

    if indent_char:
        indent_size = len(indent.split(indent_char)) - 1
        if not pindent_unit:
            pindent_unit = indent_size
        elif indent_size % pindent_unit != 0:
            return "Inconsistent indent unit"
        elif indent_size != (pindent_size - pindent_unit) and \
            indent_size != (pindent_size + pindent_unit) and \
            indent_size != pindent_size:
            return "Illegal indent step"
        pindent_size = indent_size
    return

def p_program(p):
    '''program : program statement
               | statement'''
    p[0] = []
    collect_stmts(p[0], p[1:])


### all statements

def p_statement(p):
    '''statement : command NEWLINE'''
    if isinstance(p[1], str):
        print 'Error ', p[1]
    else:
        p[0] = p[1]

def p_statement_error(p):
    '''statement : error NEWLINE'''
    e = ("Malformed statement at line", p.lineno(1), p.lexpos(1))
    p.parser.error = e

def p_statement_blank(p):
    '''statement : NEWLINE'''
    pass

### comment
def p_command_comment(p):
    '''command : COMMENT'''
    #print 'command comment ', p[1]
    pass

def get_ownerlist(target, _ownerlist):
    if _ownerlist:
        for o in _ownerlist:
            if type(o) == types.ListType:
                get_ownerlist(target, o)
            else:
                target.append(o)

### task
def p_command_task(p):
    '''command : TASKNM optstart optend optdone optownerlist optdepend optcomment'''
    tasknm = p[1]
    start = p[2]
    end = p[3]
    done = p[4]
    ownerlist = []
    get_ownerlist(ownerlist, p[5])
    dependnm = p[6]
    indent = tasknm[0:tasknm.find('[')]
    ie = check_indent_consistency(indent)
    if ie:
		raise Exception("%s : '%s'" % (ie, tasknm))
    parent = None
    p[0] = Task(parent, tasknm, start, end, done, ownerlist, dependnm)

### mile
def p_command_mile(p):
    '''command : MILENM optstart optdepend optcomment'''
    milenm = p[1]
    start = p[2]
    dependnm = p[3]
    p[0] = Milestone(milenm, start, dependnm)

### optional start
def p_optstart(p):
    '''optstart : date
                | empty'''
    p[0] = p[1]
    # print 'optstart ', p[1]

### optional end
def p_optend(p):
    '''optend : date
              | empty'''
    p[0] = p[1]
    # print 'optend ', p[1]

### optional done
def p_optdone(p):
    '''optdone : PERCENT
               | empty'''
    p[0] = p[1]
    # print 'optdone ', p[1]

### optional ownerlist
def p_optownerlist(p):
    '''optownerlist : ownerlist
                    | empty'''
    p[0] = p[1]
    # print 'optownerlist ', p[1]

### optional depend
def p_optdepend(p):
    '''optdepend : depend
                    | empty'''
    p[0] = p[1]
    # print 'optdepend ', p[1]

def p_depend(p):
    '''depend : ARROW TASKNM'''
    p[0] = p[2]
    # print 'depend ', p[1]

### optional comment
def p_optcomment(p):
    '''optcomment : COMMENT
                  | empty'''
    # print 'optcomment ', p[1]

### ownerlist
def p_ownerlist(p):
    '''ownerlist : ownerlist OWNER
                 | OWNER'''
    p[0] = p[1:]
    # print 'ownerlist ', p[1:]

### date
def p_date(p):
    '''date : YEARMONTHDAY
            | MONTHDAY
            | TERM'''
    p[0] = p[1]
    # print 'date ', p[1]

### empty

def p_empty(p):
    '''empty : '''

###  catastrophic error handler
def p_error(p):
    if not p:
        print "Syntax error at EOF"
    else:
        print "Syntax error at line %d : '%s'" % (p.lineno, p.value[:p.value.find('\n')])

parser = yacc.yacc()

def parse(data):
    parser.error = 0
    p = parser.parse(data + '\n')
    if parser.error:
        err = parser.error
        print err[0], err[1]
        return None
    return p

def test():
    data = '''
# line comment
[task 1]
[task 2] 2012/01/01 @haje01
[task 3] 2012/01/03 2012/01/05 @haje01 @lqez # tail comment
[task 4] 2012/01/01 2w 10% @lqez <- [task 3]

[task 5]
    [task 5-1] 2012/02/01 4w 30%
    [task 5-2] 
        [task 5-2-1] 2012/03/10 
        [task 5-2-2] 2012/03/20 

[task 6] 2012/04/01 4w @haje01 <- [task 5]
*mileston 1* <- [task 6]
    *mileston 1-1*
'''
    program = parse(data)
    if program:
        for task in program:
            print task

if __name__ == '__main__':
    test()

