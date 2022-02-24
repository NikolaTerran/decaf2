import ply.yacc as yacc
from decaf_lexer import tokens

def p_class_decl(p):
    '''class_decl : CLASS ID extends '{' class_body_decl '}' '''


def p_extends(p):
    '''extends : EXTENDS ID 
               | empty'''

def p_class_body_decl(p):
    '''class_body_decl : field_decl class_body_decl
                       | field_decl 
                       | method_decl class_body_decl
                       | method_decl
                       | constructor_decl class_body_decl
                       | constructor_decl '''

def p_method_decl(p):
    '''method_decl : modifier type ID '(' formals ')' block
                   | modifier type ID '(' ')' block
                   | modifier VOID ID '(' formals ')' block
                   | modifier VOID ID '(' ')' block '''

def p_constructor_decl(p):
    '''constructor_decl : modifier ID '(' formals ')' block 
                        | modifier ID '(' ')' block '''

def p_block(p):
    '''block : '{' stmts '}'
             | '{' '}'  '''

def p_stmts(p):
    '''stmts : stmt stmts
             | stmt'''

def p_stmt(p):
    '''stmt : IF '(' expr ')' stmt ELSE stmt
            | IF '(' expr ')' stmt
            | WHILE '(' expr ')' stmt
            | FOR '(' ';' expr ';'  ')' stmt
            | RETURN expr ';'
            | BREAK ';'
            | CONTINUE ';'
            | block
            | var_decl
            | ';'  '''

def p_expr(p):
    '''expr : primary '''
#            | assign
#            | new_array
#            | expr arith_op expr
#            | expr bool_op expr
#            | unary_op expr'''

def p_primary(p):
    '''primary : literal
               | THIS
               | SUPER
               | '(' expr ')'
               | NEW ID '(' arguments ')'
               | NEW ID '(' ')' '''

def p_arguments(p):
    '''arguments : expr ',' arguments 
                 | expr '''

def p_literal(p):
    '''literal : INTEGER_CONST
               | FLOAT_CONST
               | STRING_CONST
               | NULL
               | TRUE
               | FALSE'''

def p_formals(p):
    '''formals : formal_param ',' formals
               | formal_param '''

def p_formal_param(p):
    '''formal_param : type variable'''

def p_field_decl(p):
    'field_decl : modifier var_decl '

def p_modifier(p):
    '''modifier : access STATIC  
                | access '''

def p_access(p):
    '''access : PUBLIC
              | PRIVATE
              | empty '''

def p_var_decl(p):
    '''var_decl : type variables ';' '''

def p_type(p):
    '''type : INT
            | FLOAT
            | BOOLEAN
            | ID'''

def p_variables(p):
    '''variables : variable ',' variables 
                 | variable '''

def p_variable(p):
    'variable : ID'

def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print("ERROR!")
    print(p)

# Build the parser
parser = yacc.yacc(debug=True)

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
