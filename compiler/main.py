import sys
#Run "cd compiler; python main.py test.tts"
ast = {
    "include":[],
    "vars":{}
}
with open(
    sys.argv[1] #running {compile main.tts} passes ["compile","path/main.tts"] to the program (note, it only works if this is called compile.py (using things, we can compile python to x86_64 and have it as exe) (or just use main main.tts))
    ) as tocompf: #I use namef to show its the file version
    tocomp = tocompf.read()
    tocomp = tocomp.replace("\n","")
    print(tocomp)
    tmps = ""
    tmpl = []
    for i in tocomp:
        if i == ";" or i == "{" or i == "}":
            if i == "{" or i == "}":
                tmps = tmps+i
            tmpl.append(tmps)
            tmps = ""
        else:
            tmps = tmps+i
    print(tmpl)
    parsedlist = tmpl
    for i in parsedlist:
        if i.split(" ")[0] == "include":
            ast["include"].append(i.split(" ")[1])
        if i.split(" ")[0] == "func":
            tmpl =" ".join(i.split(" ")[1:]).split("(")[1].split(")")[0].split(",")
            tmpd = {}
            for j in tmpl:
                tmpd.update({j.lstrip(" ").split(" ")[1]:{"type":j.lstrip(" ").split(" ")[0]}}) #Yes, this is a monolithic code block. I can't be bothered to fix it
            ast["vars"].update({i.split(" ")[1].split("(")[0]:{
                "type":"func",
                "params":tmpd,
                "value":{}
            }})
        #Add logic for bool, func, int, str, etc.
    print(ast)
    #Process ast into compiled tetrascript