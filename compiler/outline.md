# Description/purpose
Tetrascript is to be a compiled language that compiles to the architecture in assembler/README.md
It is to make writing tetrad OS and applications for it much easier.
# Syntax
Tetrascript is designed to be C-like, but with a function type (func) that does not return anything.
```tetrascript
include sys;
func main(){
    sys.out("hello from tetrad!")
}
```
The `include` keyword is used to tell the compiler that the specified module should be compiled as part of the file.
The entrypoint function is `main`.
Calling a function from a module is syntaxically similar to python, except with a semicolon at the end of lines.
# Semicolons and curly brackets:
## Semicolons are needed in these places:
+ At the end of a function call only if there is another one after within the same code section.
+ Between variable and function declorations.
+ Between module imports
## They are not required:
+ Between 2 function defenitions (`func other(){}funct main(){}` can be relatively easily seen as seperate)
+ At the end of a code section (`func main(){sys.out()}` can be seen easily as seperate)
## Curly brackets are for:
+ Function variable definitions
+ The `do` param (see later)

# Special builtins:
+ `runasm(<str>)` Compiler alters the params here but otherwise leaves it exactly the same
+ `jump(<int>)` Compiler replaces with a corrected jump call
The `do` param: see later

# The `do` param
Always only allows a function. The function is passed in via curly braces after the rest of the function. The `do` parameter must be declared in CAPS and can be called like any function within your function
eg.
```tetrascript
include sys;
func usesdo(DO){
    DO()
}
func main(){
    usesdo(){
        sys.out("I am passed into the 'usesdo' function as the DO param")
    }
}
```
