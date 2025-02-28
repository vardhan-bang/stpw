from random import randint, choice

comparison = ['<', '>', '<=', '>=', '==', '!=']
arithmetic = ['+=', '-=']
unary = ['++', '--']

int_min = 0
int_max = 100 

def random_int():
    return randint(int_min, int_max)

def init_statement():
    return f"int num = {random_int()};"

def ari_statement():
    return f"num {choice(arithmetic)} {random_int()};"

def if_statement():
    return f"if(num {choice(comparison)} {random_int()})"

def for_statement(temp):
    return f"for(int {temp} = {random_int()}; {temp} {choice(comparison)} {random_int()}; {temp}{choice(unary)})"