# Function calls
When a function is called, it pushes the params to the stack, which are then managed by the function.\
Return is then pushed to the stack after execution. If the function does not call return, then return 0 should be inserted by the compiler.
# Runtime Linker (RTL)
Part of the kernel which runs through programs when loaded, handles program localised memory, the require keyword\
Runs through the target program (see syscall/loadfile) and alters the params of pop, push, jump, etc so that that program stays contained in it's own sandboxed memory.
# Syscall
## How???
Yes, we use the whole "1 based indexing but pop 0 is still a thing" and the RTL
```
.code:
            ;some code to load the values
  pop 0     ;kernel runtime linker runs through the program when loaded into memory, but when it sees this, it toggles the linker
            ;it does, however keep iterating through
  pop 10    ;then use these things
  pop 11
  pop 0     ;then turn the RTL back on
```
## Syscalls
The system will call the function with these params when you move true (255) to 10 when syscall mode is on
### Loadfile
Loads a file (specified by $FIL) from the drive specified by $DRV to memory decided by kernel\
Also adds a key to the kernel protected part of ram to say it's loaded and it's address\
 1: $CAL exp: 0 ;Loadfile is identified by 0\
 2: $DRV DEF: ? ;Which drive it should pull from. (equivilant of windows C:/)\
 3: $FIL REQ    ;The actual file path. (the rest of the path (/boot/hello.txt))
 ### Clearmem
 #TODO
