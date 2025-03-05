# stpw

## Steps:
### 1. Create and activate virtual environment and install dependencies using requirements.txt
### 2. Generate c files:
``` bash
make c n={number of files}
```
### 3. Generate assembly files
``` bash
make asm cc={c compiler}
```
### 4. Generate datasets
``` bash
make data
```
### 5. To delete all temporary files
``` bash
make clean
```
