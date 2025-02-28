import os
import subprocess

c_files_dir = 'c_files'
assembly_dir = 'assembly'

def generate_assembly(c_file):
    filename_without_extension = os.path.splitext(c_file)[0]
    c_file_path = os.path.join(c_files_dir, c_file)
    assembly_file_path = os.path.join(assembly_dir, f'{filename_without_extension}.s')
    subprocess.run(['clang', '-S', c_file_path, '-o', assembly_file_path])

for c_file in sorted(os.listdir(c_files_dir)):
    print(f'Generating assembly for {c_file}...')
    generate_assembly(c_file)
    print(f'Assembly code saved to {os.path.join(assembly_dir, c_file.replace(".c", ".s"))}')

print("Assembly code generated for all files.")
