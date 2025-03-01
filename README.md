# stpw

## Steps:
1. ### Create and activate virtual environment and install dependencies using requirements.txt
2. ### Generate c files:
    ``` bash
    make c n={number of files}
    ```
3. ### Generate assembly files
    ``` bash
    make asm cc={c compiler}
    ```
4. ### To delete all .c and .s files
    ```
    make clean
    ```
