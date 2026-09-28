import sys
with open(
    sys.argv[1] #running {compile main.tts} passes ["compile","path/main.tts"] to the program (note, it only works if this is called compile.py (using things, we can compile python to x86_64 and have it as exe))
    ) as tocompf: #I use namef to show its the file version
    tocomp = tocompf.read()
    #PUT STUFF HERE!!!