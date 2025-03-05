import csv, os, sys
import pandas as pd
from categories import instruction_types

architecture = sys.argv[1]


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
        type_seq.append(instruction_types[instruction])
    return type_seq

def generate_value_seq(asm_list):
    value_seq = []
    for line in asm_list:
        for component in line[1:]:
            if component[0] == '$':
                value_seq.append(int(component[1:]))

    return value_seq

snippet_types_df = pd.read_csv("datasets/snippet_type.csv")

asm_files = os.listdir("asm_files")
asm_files.remove(".gitkeep")
asm_files = sorted(asm_files)
asm_files_df = pd.DataFrame(data={'asm_file': asm_files})
asm_files_df.to_csv("datasets/asm_files.csv", index=False)

asm_clean_df = pd.DataFrame(data = asm_files_df['asm_file'].apply(clean_asm))
asm_clean_df = asm_clean_df.rename(columns = {'asm_file':'asm_clean'})
asm_clean_df.to_csv("datasets/asm_clean.csv", index=False)

asm_seq_df = pd.DataFrame(data = asm_clean_df["asm_clean"].apply(generate_asm_sequence))
asm_seq_df = asm_seq_df.rename(columns = {"asm_clean" :"asm_seq"})
asm_seq_df.to_csv("datasets/asm_seq.csv", index=False)

asm_type_seq_df = pd.DataFrame(data = asm_seq_df["asm_seq"].apply(generate_asm_type_sequence))
asm_type_seq_df = asm_type_seq_df.rename(columns = {"asm_seq" : "asm_type_seq"})
asm_type_seq_df.to_csv("datasets/asm_type_seq.csv", index=False)

value_seq_df = pd.DataFrame(data = asm_clean_df["asm_clean"].apply(generate_value_seq))
value_seq_df = value_seq_df.rename(columns = {"asm_clean" : "value_seq"})
value_seq_df.to_csv("datasets/value_seq.csv", index=False)