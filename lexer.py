import ply.lex as lex

# Reserved words
reserved = {
    'perguntei?' : 'IF',
    'emole' : 'ELSE',
    'naogrita' : 'WHILE',
    'bobesponja' : 'PRINT',
    'grite' : 'DO'
}

# List of token names.
tokens = [
    'ID',
    'ATT',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE', 
    'LPAREN',
    'RPAREN',
    'LKEY',
    'RKEY',
    'TERMINATOR',
    'GTHAN',
    'LTHAN',
    'GETHAN',
    'LETHAN',
    'EQUAL'
] + list(reserved.values())


# Rules using regEx for simple tokens.
t_ATT = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

# Separators
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LKEY = r'\{'
t_RKEY = r'\}'

# End of sentence
t_TERMINATOR  = r';'

# Conditionals
t_GTHAN = r'>'
t_LTHAN = r'<'
t_GETHAN = r'>='
t_LETHAN = r'<='


# Regex rule for with some action code.
def t_NUMBER(t):
    r"""\d+"""
    t.value = int(t.value)
    return t

def t_IF(t):
    r"""perguntei\?"""
    t.type = reserved.get(t.value)
    return t

def t_ELSE(t):
    r"""emole"""
    t.type = reserved.get(t.value)
    return t

def t_WHILE(t):
    r"""naogrita"""
    t.type = reserved.get(t.value)
    return t

def t_DO(t):
    r"""grite"""
    t.type = reserved.get(t.value)
    return t

def t_PRINT(t):
    r"""bobesponja"""
    t.type = reserved.get(t.value)
    return t

# Regex action rule to check if the ID is a reserved word or not
def t_ID(t):
    r"""[a-zA-Z_][a-zA-z_0-9]*"""
    t.type = reserved.get(t.value, 'ID')
    return t


# Rule to track line numbers
def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)

# Ignore the following rule
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}\n\tlinha {t.lineno} posição {t.lexpos} token {t.type}")

    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()