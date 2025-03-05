import csv, os
import pandas as pd

instruction_types = {
    
}

def clean_asm(asm_file):
    file = open(f"../asm_files/{asm_file}", 'r')
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



snippet_types_df = pd.read_csv("datasets/snippet_type.csv")

asm_files = os.listdir("../asm_files")
asm_files.remove(".gitkeep")
asm_files = sorted(asm_files)
snippet_types_df['asm_file'] = asm_files

asm_clean = pd.DataFrame(data = snippet_types_df['asm_file'].apply(clean_asm))
asm_clean = asm_clean.rename(columns = {'asm_file':'asm_clean'})
asm_clean.to_csv("../datasets/asm_clean.csv", index=False)

asm_seq = pd.DataFrame(data = asm_clean['asm_clean'].apply(generate_asm_sequence))
asm_seq = asm_seq.rename(columns = {"asm_clean":"asm_seq"})
asm_seq.to_csv("../datasets/asm_seq.csv", index=False)