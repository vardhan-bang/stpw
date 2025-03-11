import os, sys

c_compiler = sys.argv[1]
number_of_files = int(sys.argv[2])

for filenum in range(number_of_files):
    os.system(f"{c_compiler} -S c_files/{filenum:05d}.c -o asm_files/{filenum:05d}.s ")
    print(f"Generated Asm files: {filenum}/{number_of_files}", end='\r')
print(f"Generated Asm files: {number_of_files}/{number_of_files}")