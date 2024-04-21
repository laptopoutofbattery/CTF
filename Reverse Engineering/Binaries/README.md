### Binaries

Reversing binaries (executables).

Important terms:
- Position Independent Executables (PIE): means every time the file is run it gets loaded into a different memory address
- Address Space Layout Randomisation (ASLR): guards against buffer overflow attacks by randomising location where system executables are loaded into memory

Useful links:
- https://hex-rays.com/products/ida/support/tutorials/
- https://hex-rays.com//products/ida/support/freefiles/IDA_Pro_Shortcuts.pdf
- https://cs.brown.edu/courses/cs033/docs/guides/gdb.pdf
- https://github.com/ViRb3/z3-python-ctf