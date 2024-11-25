import ply.yacc as yacc
from jinja2.nodes import Break
import sys

from lexer import tokens


# Context-Free Grammar definition.
def p_start(p) :
    """start : statement
             | start statement             
             """
    p[0] = p[1:]

# Possible statements
def p_statements(p):
    """statement : if
                 | print
                 | dowhile
                 | while
                 | att"""

# Statement definition
def p_if(p):
    """if : IF LPAREN bool RPAREN LKEY start RKEY ELSE LKEY statement RKEY"""
    p[0] = ('if', p[3], p[6],'else',p[10])

def p_dowhile(p):
    """dowhile : DO LKEY start RKEY WHILE LPAREN bool RPAREN TERMINATOR"""
    p[0] = ('dowhile',p[3],p[7])

def p_while(p):
    """while : WHILE LPAREN bool RPAREN LKEY start RKEY"""
    p[0] = ('while', p[3], p[6])

def p_print(p):
    """print : PRINT LPAREN expression RPAREN TERMINATOR"""
    p[0] = ('print', p[3])

def p_statement_expression(p):
    """att : ID ATT expression TERMINATOR
                 | ID ATT bool TERMINATOR"""
    p[0] = (p[1], p[3])

# Binary operations and boolean operations
def p_bool_expresion(p):
    """bool : term LTHAN term
            | term GTHAN term
            | term LETHAN term
            | term GETHAN term
            | term EQUAL term"""
            
    p[0]  = (p[1], p[2], p[3])

def p_expression_bop(p):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  """
    p[0] = (p[1], p[2], p[3])

def p_expression_group(p):
    """expression : LPAREN expression RPAREN"""
    p[0] = p[2]

# Terminator
def p_expression_num(p):
    """expression : term"""
    p[0] = p[1]

def p_term_numid(p):
    """term : NUMBER 
            | ID"""
    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    if p:
         print(f"Syntax error at token {p.type} line {p.lineno}")
         parser.errok()
    else:
         print("Syntax error at EOF")


# Analyse the given file from the cl argument
path = sys.argv[1]

with open(path, 'r') as f:
    data = f.read()
# Build parser
parser = yacc.yacc()


info = parser.parse(data)
if info :
    print('Perfect code!!!')
else:
    print(info)
