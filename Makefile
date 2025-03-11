# gcc or clang
CC = clang
# x86 or arm
ARCH = arm
#number of data points
N = 100
#min numeric value in c snippets
MIN_VALUE = 1
#max numeric value in c snippets
MAX_VALUE = 100

data:
	python3 src/data_generation/generate_data.py $(ARCH) $(CC) $(N)

asm:
	python3 src/generate_asm.py $(CC)

c:
	python3 src/generate_c.py $(N) $(MIN_VALUE) $(MAX_VALUE) 

clean:
	rm -f c_files/*.c
	rm -f asm_files/*.s
	rm -f datasets/*.csv