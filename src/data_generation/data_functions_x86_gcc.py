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

operator_instructions = ("jle", "jne", "je", "jg", "addl", "subl")

def clean_asm(asm_file):
    file = open(f"asm_files/{asm_file}", 'r')
    code = file.read().split('\n')
    code = [line.strip() for line in code]
    code = code[code.index('.cfi_def_cfa_register 6') + 1: code.index('movl\t$0, %eax')]
    code = [line.split() for line in code]
    for i, line in enumerate(code):
        temp = [elem[:-1] if elem[-1]==',' else elem for elem in line]
        code[i] = temp
    return code

def generate_asm_sequence(asm_list):
    asm_seq = []
    for line in asm_list:
        instruction = line[0]
        if instruction[:2] == ".L":
            asm_seq.append('label')
        else:
            asm_seq.append(instruction)
    return asm_seq

def generate_asm_type_sequence(asm_seq):
    type_seq = []
    for instruction in asm_seq:
        if instruction in instruction_types.keys():
            type_seq.append(instruction_types[instruction])
    return type_seq

def generate_value_sequence(asm_list):
    value_seq = []
    for line in asm_list:
        for component in line[1:]:
            if component[0] == '$':
                value_seq.append(int(component[1:]))

    return value_seq

def generate_operator_sequence(asm_seq):
    operator_seq = []
    for instruction in asm_seq:
        if instruction in operator_instructions:
            operator_seq.append(instruction)

    return operator_seq