import ply.yacc as yacc
from jinja2.nodes import Break

from lexer import tokens

with open('example_scripts/basic.txt', 'r') as f:
    data = f.read()

# Context-Free Grammar definition.
def p_start(p) :
    """start : statement
             | start statement
             
             """
    p[0] = p[1:]

# For boolean statements and operators
def p_statement_bool(p):
    """statement : IF LPAREN bool RPAREN LKEY statement RKEY ELSE LKEY statement RKEY"""
    p[0] = ('if', p[3], p[6],'else',p[10])

def p_bool_expresion(p):
    """bool : term LTHAN term
            | term GTHAN term
            | term LETHAN term
            | term GETHAN term"""
    p[0]  = (p[1], p[2], p[3])

# Loops
def p_statement_while(p):
    """statement : WHILE LPAREN bool RPAREN LKEY statement RKEY
                 """
    p[0] = ('while', p[3], p[6])

def p_statement_dowhile(p):
    """statement : DO LKEY statement RKEY WHILE LPAREN bool RPAREN TERMINATOR"""

# Variable assigning and binary operations
def p_statement_expression(p):
    """statement : ID ATT expression TERMINATOR"""
    p[0] = (p[1], p[3])
    
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
    linhas = data.splitlines()
    print(f'Erro de sintaxe na linha {p.lineno - 1} -> {linhas[p.lineno - 2]}')

# Build parser
parser = yacc.yacc()


print(parser.parse(data))
