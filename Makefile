all:
	python3 generate.py

clean:
	rm c_files/*.c
	rm asm_files/*.s