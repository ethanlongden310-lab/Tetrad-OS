# Assembler
This is an assembler program for the virtual machine.
# Expected format of toassemble:
.code:
  place your code here
.mem:
  place constant values here
note that the assembler adjusts the values for most instructions based on where it puts .mem, so push 1 will always apply to the first entry of .mem
# Opcodes:
0: push a     //pushes value at $a to stack
1: pop a      //pops stack to $a
2: jmp a      //sets program counter to $a
3: jmp0 a     //pops stack, if the value popped is 0, it jumps to $a, otherwise, it just continues
4: halt       //halts program execution
5: add a      //pops stack, adds $a to the popped value and the pushes the new value
6: sub a      //S.A.A but subtraction
7: not        //applies bitwise not to the last item on the stack
8: or a       //applies bitwise or to the top of stack and value at $a
9: and a      //s.a.a but and
10: xor a     //s.a.a but xor
11: hard p    //pops stack and sends popped value to specified port ($p)
12: exarg a   //on the next instruction, the arguement is equal to (p<<8|a). this stacks
