import sys

instruction_types = {

    #MEMORY READ/WRITE INSTRUCTIONS
    "movl": 0,
    #JUMP INSTRUCTIONS
    "jmp": 1,
    "jle": 1,
    "jne": 1,
    "je": 1,
    "jg": 1,
    #ARITHMETIC INSTRUCTIONS
    "addl": 2,
    "subl": 2,
    #COMPARISON INSTRUCTIONS
    "cmpl": 3,
    #LABEL
    "label": 4
}