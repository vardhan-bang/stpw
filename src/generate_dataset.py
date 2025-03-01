import csv, os

asm_files = os.listdir("asm_files")
asm_files.remove(".gitkeep")
asm_files = sorted([f"asm_files/{i}" for i in asm_files])
print(asm_files)