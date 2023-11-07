from ply.yacc import yacc
from lexer import tokens
from expression import *

__all__ = ["parser", "parse_and_print"]


# Definimos una función para cada producción de la gramática

# TODO: Modificar las producciones para parsear correctamente el lenguaje

def p_expression_plus(p):
    '''
    expression : expression PLUS term
    '''
    p[0] = Sum(p[1], p[3])

def p_expression_minus(p):
    '''
    expression : expression MINUS term
    '''
    p[0] = Sub(p[1], p[3])

def p_expression_term(p):
    '''
    expression : term
    '''
    p[0] = Term(p[1])

def p_term_star(p):
    '''
    term : term STAR factor
    '''
    p[0] = Prod(p[1], p[3])

def p_term_div(p):
    '''
    term : term DIV factor
    '''
    p[0] = Div(p[1], p[3])

def p_term_factor(p):
    '''
    term : factor
    '''
    p[0] = Factor(p[1])

def p_factor_negative(p):
    '''
    factor : MINUS factor
    '''
    p[0] = Neg(p[2])

def p_factor_id(p):
    '''
    factor : ID
    '''
    p[0] = Id(p[1])

def p_term_p(p):
    '''
    factor : POPEN expression PCLOSE
    '''
    p[0] = Par(p[2])

# def p_expression_empty(p):
#     '''
#     expression : 
#     '''
#     


# Manejo de errores

def p_error(p):

    if p:
        raise ParseError(
            f'Unexpected token {p.value!r} at position {p.lexpos}')
    else:
        raise ParseError(f'Unexpected end of expression')


class ParseError(Exception):
    pass


parser = yacc()


def parse_and_print(string):
    # TODO: Modificar, si es necesario, para imprimir correctamente el resultado
    # de la traducción
    parse_result = parser.parse(string)
    print(parse_result.evaluate())
