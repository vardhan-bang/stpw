instruction_types = {
    #OTHER
    "other": 0,
    #MEMORY READ/WRITE INSTRUCTIONS
    "movl": 1,
    #JUMP INSTRUCTIONS
    "jmp": 2,
    "jle": 2,
    "jne": 2,
    "je": 2,
    "jg": 2,
    #ARITHMETIC INSTRUCTIONS
    "addl": 3,
    "subl": 3,
    #COMPARISON INSTRUCTIONS
    "cmpl": 4,
    #LABEL
    "label": 5
}

operator_instructions = ("jle", "jne", "je", "jg", "addl", "subl")
ignored_instructions = ("other", "label")

def clean_asm(asm_file):
    file = open(f"asm_files/{asm_file}", 'r')
    code = file.read().split('\n')
    code = [line.strip().split() for line in code]
    code = [line for line in code if line]
    for i, line in enumerate(code):
        temp = [elem[:-1] if elem[-1]==',' else elem for elem in line]
        code[i] = temp
    return code

def generate_asm_sequence(asm_list):
    asm_seq = []
    for line in asm_list:
        instruction = line[0]
        if instruction[0] == '.':
            if instruction[-1] == ':':
                asm_seq.append("label")
            else:
                asm_seq.append("other")
        elif instruction in instruction_types.keys():
            asm_seq.append(instruction)
        elif instruction[-1] == ':':
            asm_seq.append("label")
        else:
            asm_seq.append("other")
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

def generate_operator_sequence(asm_list):
    operator_seq = []
    for line in asm_list:
        for instruction in line:
            if instruction in operator_instructions:
                operator_seq.append(instruction)

    return operator_seq