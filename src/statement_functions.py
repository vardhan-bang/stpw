from random import randint, choice
import sys

min_value = int(sys.argv[2])
max_value = int(sys.argv[3])

comparison = ['<', '>', '<=', '>=', '==', '!=']
arithmetic = ['+=', '-=']
unary = ['++', '--']

def init_statement():
    return f"int num = {randint(min_value, max_value)};"

def ari_statement():
    return f"num {choice(arithmetic)} {randint(min_value, max_value)};"

def if_statement():
    return f"if(num {choice(comparison)} {randint(min_value, max_value)})"

def for_statement(temp):
    return f"for(int {temp} = {randint(min_value, max_value)}; {temp} {choice(comparison)} {randint(min_value, max_value)}; {temp}{choice(unary)})"