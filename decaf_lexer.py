# name: Tianrun(Terran) Liu, netid: tianruliu, Student ID: 112838591
# courtsy of Mr. David M. Beazley and Mr. Quinten Yearsley who wrote calclex.py which is what this file mostly based off from.

import ply.lex as lex
import sys

reserved = {
    'boolean' : 'BOOLEAN',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'class' : 'CLASS',
    'do' : 'DO',
    'else' : 'ELSE',
    'extends' : 'EXTENDS',
    'false' : 'FALSE',
    'float' : 'FLOAT',
    'for' : 'FOR',
    'if' : 'IF',
    'int' : 'INT',
    'new' : 'NEW',
    'null' : 'NULL',
    'private' : 'PRIVATE',
    'public' : 'PUBLIC',
    'return' : 'RETURN',
    'static' : 'STATIC',
    'super' : 'SUPER',
    'this' : 'THIS',
    'true' : 'TRUE',
    'void' : 'VOID',
    'while' : 'WHILE'
}

tokens = [ 'INTEGER_CONST', 'FLOAT_CONST', 'STRING_CONST', 'ID'] + list(reserved.values())

# Token matching rules are written as regexs
t_BOOLEAN = r'boolean'
t_BREAK = r'break'
t_CONTINUE = r'continue'
t_CLASS = r'class'
t_DO = r'do'
t_ELSE = r'else'
t_EXTENDS = r'extends'
t_FALSE = r'false'
t_FLOAT = r'float'
t_FOR = r'for'
t_IF = r'if'
t_INT = r'int'
t_NEW = r'new'
t_NULL = r'null'
t_PRIVATE = r'private'
t_PUBLIC = r'public'
t_RETURN = r'return'
t_STATIC = r'static'
t_SUPER = r'super'
t_THIS = r'this'
t_TRUE = r'true'
t_VOID = r'void'
t_WHILE = r'while'

def t_ID(t):
    r'\b[a-zA-Z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_COMMENT(t):
    r'(\/\/[^\n]*)|(\/\*.*?(?=\*\/)\*\/)'
    pass

#def t_INTEGER_CONST(t):
#    r'-?\d+'
#    t.value = int(t.value)
#    return t

def t_FLOAT_CONST(t):
    r'-?\d+\.\d+([e|E](\-|\+?)\d+)?'
    t.value = float(t.value)
    return t

def t_INTEGER_CONST(t):
    r'-?\d+'
    t.value =  int(t.value)
    return t

def t_STRING_CONST(t):
    r'"[^"]*"'
    t.value = str(t.value)
    return t

# Ignored characters
t_ignore = ' \t'

# Ignored token with an action associated with it
def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

# Error handler for illegal characters
def t_error(t):
     print('Illegal character {} at line {}'.format(t.value[0], t.lineno))
     exit(1)

literals = [ '+','-','*','/', '{', '}', '[', ']', '(', ')' , ',', ';', '.' ]

# Build the lexer object
lexer = lex.lex()

# # Give the lexer some input
# try:
#     global f 
#     f = open(sys.argv[1], "r")    
# except:
#     try:
#         f = open(input("Please enter a valid path to ssm source file:\n"))
#     except:
#         print("File not found")
#         raise FileNotFoundError from None

# data = f.read()

# lexer.input(data)

# # Tokenize
# toks = []

# while True:
#     tok = lexer.token()
#     if tok:
#         print(tok)
#         toks.append(tok)
#     else:
#         break      # No more input

