import ply.lex as lex
import ply.yacc as yacc

'''
compiladorELA.py

Identificadores aceptados
var = variable
const = constante

palabras reservadas
var
const
int 
float
char
string

Tipos de datos
integer
float
char
string

Operadores Aritmeticos
+
+
*
/

Operadores Relacionales
<
>
<=
>=
==

Operadores Logicos
or
and
true
false

Caracteres especiales 
0
; 
{}
()

Sentencias Controladores
IF()
WHILE()
DO - WHILE()
FOR(int x; x <= 0; x++)
'''



tokens = (
    #Palabras reservadas
    'VAR'
    'CONST'
    'INT'
    'FLOAT'
    'CHAR'
    'STRING'
    #Operadores aritmeticos
    'SUM'
    'MINUS'
    'DIV'
    'MULT'
    #Operadores logicos
    'LESS'
    'LESSEQ'
    'EQ'
    'MORE'
    'MOREEQ'
    'OR'
    'AND'
    #Booleanos
    'TRUE'
    'FALSE'
    #Simbolos
    'PARIZQ'
    'PARDER'
    'CORIZQ'
    'CORDER'
    'SEMICOL'
    #Operadores
    'IF'
    'WHILE'
    'DO'
    'FOR'
    #Asignar
    'ASIGN'
)

t_VAR = r'\bvar\b'
t_CONST = r'\bconst\b'
t_INT = r'\bint\b'
t_FLOAT = r'\bfloat\b'
t_CHAR = r'\bchar\b'
t_STRING = r'\bstring\b'
t_SUM = r'\+'
t_MINUS = r'\-'
t_DIV = r'/'
t_MULT = r'\*'
t_LESS = r'<'
t_LESSEQ = r'<='
t_EQ = r'=='
t_MORE = r'>'
t_MOREEQ = r'>='
t_OR = r'\|\|'
t_AND = r'\&\&'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\{'
t_CORDER = r'\}'
t_SEMICOL = r';'
t_ASIGN = r'='


def t_VAR(t):
    r'\bvar'
    return t;

def t_CONST(t):
    r'const'
    return t

def t_INT(t):
    r''
    t.value = int(t.value)
    return t;

def t_FLOAT(t):
    