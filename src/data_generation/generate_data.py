import csv, os, sys
import pandas as pd

architecture = sys.argv[1]
compiler = sys.argv[2]

if architecture == "x86":
    if compiler == "gcc":
        from data_functions_x86_gcc import *
    elif compiler == "clang":
        from data_functions_x86_clang import *
elif architecture == "arm":
    if compiler == "gcc":
        from data_functions_arm_gcc import *
    elif compiler == "clang":
        from data_functions_arm_clang import *

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

value_seq_df = pd.DataFrame(data = asm_clean_df["asm_clean"].apply(generate_value_sequence))
value_seq_df = value_seq_df.rename(columns = {"asm_clean" : "value_seq"})
value_seq_df.to_csv("datasets/value_seq.csv", index=False)

operator_seq_df = pd.DataFrame(data = asm_seq_df["asm_seq"].apply(generate_operator_sequence))
operator_seq_df = operator_seq_df.rename(columns = {"asm_seq": "operator_seq"})
operator_seq_df.to_csv("datasets/operator_seq.csv", index = False)

data_df = pd.DataFrame(data = {"input": asm_type_seq_df["asm_type_seq"], "target": snippet_types_df["snippet_type"]})
data_df.to_csv("datasets/data.csv", index = False)
