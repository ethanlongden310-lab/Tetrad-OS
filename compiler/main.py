import sys
with open(
    sys.argv[1] #running {compile main.tts} passes ["compile","path/main.tts"] to the program (note, it only works if this is called compile.py (using things, we can compile python to x86_64 and have it as exe) (or just use main main.tts))
    ) as tocompf: #I use namef to show its the file version
    tocomp = tocompf.read()
    print(tocomp)
    #code goes here