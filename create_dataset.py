import os
import csv


c_files_dir = 'c_files'
assembly_files_dir = 'assembly'
dataset = []

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()



c_files = sorted([f for f in os.listdir(c_files_dir)])
assembly_files = sorted([f for f in os.listdir(assembly_files_dir)])


for c_file, asm_file in zip(c_files, assembly_files):
    c_file_path = os.path.join(c_files_dir, c_file)
    asm_file_path = os.path.join(assembly_files_dir, asm_file)
    c_code = read_file(c_file_path)
    asm_code = read_file(asm_file_path)
    dataset.append((c_code, asm_code))


output_file = 'dataset.csv'
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['C Code', 'Assembly Code']) 
    for c_code, asm_code in dataset:
        writer.writerow([c_code, asm_code])

print(f"Dataset saved to {output_file}")
