import ply.yacc as yacc
from decaf_lexer import tokens


# def p_class_decl(p):
#     '''class_decl : CLASS id extends
#             '{' class_body_decl '}'
#     '''

def p_class_decl(p):
    '''class_decl : CLASS ID extends'''


def p_extends(p):
    '''extends : EXTENDS ID 
               | empty'''

# def p_class_body_decl(p):
#     '''class_body_decl : field_decl class_body_decl
#             | field_decl'''

# def p_field_decl(p):
#     'field_decl : modifier var_decl'

# def p_modifier(p):
#     '''modifier : access STATIC 
#                 | access'''

# def p_var_decl(p):
#     'var_decl : type variables'

# def p_type(p):
#     '''type : integer_const
#             | float_const
#             | BOOLEAN
#             | id'''

# def p_variables(p):
#     'variables : variable variables'

# def p_variable(p):
#     'variable : id'

# def p_access(p):
#     '''access: PUBLIC
#             | PRIVATE
#             | empty'''

def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

f = open("dummy.decaf", "r")
# while True:
#     try:
#         s = input("> ")
#     except EOFError:
#         break
#     if not s: 
#         continue
result = parser.parse(f.read())
print(result)