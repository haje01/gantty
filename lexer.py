
from ply import lex

states = (
    ('task', 'exclusive'),
)

tokens = (
    'TASKNM',
    'NEWLINE',
    'YEARMONTHDAY',
    'MONTHDAY',
    'TERM',
    'PERCENT',
    'OWNER',
    'COMMENT',
    'ARROW',
)

t_task_YEARMONTHDAY = r'\d{4}/\d{2}/\d{2}'
t_task_MONTHDAY = r'\d{4}/\d{2}/\d{2}'
t_task_TERM = r'\d+[hdw]'
t_task_PERCENT = r'1?\d{1,2}%'
t_task_OWNER = r'@[\S]+'
t_task_ignore = ' \t'
t_task_ARROW = r'<-'

def t_COMMENT(t):
    r'\#.*'
    t.lexer.push_state('task')
    return t

def t_task_COMMENT(t):
    r'\#.*'

def t_TASKNM(t):
    r'\s*\[[^\]]+\]'
    t.lexer.push_state('task')
    return t

def t_task_TASKNM(t):
    r'\[[^\]]+\]'
    return t

def t_task_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    t.lexer.pop_state()
    return t

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t

def t_error(t):
    print 'Illegal character ', t.value[0]
    t.lexer.skip(1)

def t_task_error(t):
    print 'Illegal task character ', t.value[0]
    t.lexer.skip(1)

lexer = lex.lex()

