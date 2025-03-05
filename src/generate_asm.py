import os, sys

if sys.argv[1]:
    c_compiler = sys.argv[1]

num_files = len(os.listdir("c_files")) - 1

for filenum in range(num_files):
    os.system(f"{c_compiler} -S c_files/{filenum:05d}.c -o asm_files/{filenum:05d}.s ")