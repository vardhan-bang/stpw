model:
	jupyter lab notebooks/model.ipynb

asm:
	python3 src/generate_asm.py $(cc)

c:
	python3 src/generate_c.py $(n)

clean:
	rm -f c_files/*.c
	rm -f asm_files/*.s