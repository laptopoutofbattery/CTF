x86-64 assembly language
-
x86-64 refers to the 64-bit version of the x86 CPU architecture implemented by many CPU manufacturers.  
Assembly programs consist of an arrangement of instructions, which are executed by the CPU to interact with memory and registers.  
- Instructions are operations performed by the CPU
- Memory refers to virtual memory storage for the running program
    - CPU: registers
    - RAM: heap and stack
    - Hard drive
- Registers are internal memory storage locations included in the processor (places that the processor can store memory, kind of like variables in code)
    - Registers are very fast and small as they are on the CPU and can be directly accessed
    - Some registers have special meaning (e.g. ESP, EBP, EIP)
    - Some registers are general purpose (e.g. EAX, EBX, ECX)

Specific registers:
- rbp: Base Pointer, points to the bottom of the current stack frame
- rsp: Stack Pointer, points to the top of the current stack frame
- rip: Instruction Pointer, points to the instruction to be executed

General purpose registers:
| 8 Byte Register | Lower 4 Bytes | Lower 2 Bytes | Lower Byte |
|-----------------|---------------|---------------|------------|
|   rbp           |     ebp       |     bp        |     bpl    |
|   rsp           |     esp       |     sp        |     spl    |
|   rip           |     eip       |               |            |
|   rax           |     eax       |     ax        |     al     |
|   rbx           |     ebx       |     bx        |     bl     |
|   rcx           |     ecx       |     cx        |     cl     |
|   rdx           |     edx       |     dx        |     dl     |
|   rsi           |     esi       |     si        |     sil    |
|   rdi           |     edi       |     di        |     dil    |
|   r8            |     r8d       |     r8w       |     r8b    |
|   r9            |     r9d       |     r9w       |     r9b    |
|   r10           |     r10d      |     r10w      |     r10b   |
|   r11           |     r11d      |     r11w      |     r11b   |
|   r12           |     r12d      |     r12w      |     r12b   |
|   r13           |     r13d      |     r13w      |     r13b   |
|   r14           |     r14d      |     r14w      |     r14b   |
|   r15           |     r15d      |     r15w      |     r15b   |


Some instructions: 
| Instruction | What it does | Syntax |
|-------------|--------------|--------|
| nop         | does nothing | `nop`  |
| mov         | moves values around | `mov eax, 4` |
| add         | adds the values, stores sum in first argument | `add eax, 5` |
| sub         | subtracts the first value by the second value, stores result in first argument | `sub eax, 5`|
| mul         | multiplies the value in `eax` by the given argument, most significant 32 bits of result stored in `edx`, least significant 32 bits of result sored in `eax` | `mul 5` |
| div         | divides the value in `eax` by the given argument, stores quotient in `eax` and remainder in `edx` | `div 5` |
| xor         | xors the two arguments, stores result in first argument | `xor eax, 5` |
| jmp         | jumps to an instruction address (can be absolute or relative), used to redirect code execution | `jmp 0x602010` |
| jz, jnz     | conditional jumps: `jz` jumps if zero flag is set, reverse for `jnz` | same as `jmp` |
| push, pop   | stack operations: push adds value of the argument to the stack, pop removes the first value on the stack and stores it in the argument | `push`/`pop` `eax` |
| call        | moves the return address on top of the stack, jumps to whatever address it is given | `call function` |
| ret         | returns from `call` to the pushed return address and continues code execution from there | `ret` |


<br></br>
  
Some cool resources:  
[omu training ASM (x86-64)](https://omu.rce.so/lessons/asm-x86-64/introduction)  
[Nightmare](https://guyinatuxedo.github.io/01-intro_assembly/assembly/index.html)  
[x86 Assembly Guide](https://www.cs.virginia.edu/~evans/cs216/guides/x86.html)  