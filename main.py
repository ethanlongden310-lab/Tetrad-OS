#COPY ME
#write in file "toassemble", navigate to the folder with both files in and then run the python file
#then, import the output.txt file into the boot list (not ram or it'll be wiped when you start the file)
#you must have a .code: and .mem: area
#put your code in .code and your starting constants in .mem
#1.2
opcodes = {
    "push":0,
    "pop":1,
    "jmp":2,
    "jmp0":3,
    "halt":4,
    "add":5,
    "sub":6,
    "not":7,
    "or":8,
    "and":9,
    "xor":10,
    "hard":11,
    "exarg":12
}
charcodes = ["",1,2,2,3,4,5,6,7,8,9,0,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","!"]
charcodes = charcodes+[""for i in range(255)]
charcodes[255] = "*" #this is the std::eof character to make stnd (scratch picked up on it so I added an n) flush stdstack to stdout
e=[]
d=[]
exempt=[
    11,
    12,
    2,
    3,
    4,
]
a=[]
last = 0
memoff = 0
inmem = False
incode = False
with open("toassemble") as tasmf:
    tasm = tasmf.readlines()
    for l in tasm:
        i=l.strip()
        print(i)
        if ".code:" in i:
            incode = True
            inmem = False
            continue
        elif ".mem:" in i:
            #print("in mem")
            memoff = tasm.index(l)
            incode = False
            inmem = True
            continue
        if inmem:
            #print(f"memory: {i}")
            if i:
                try: e.append(charcodes.index(i))
                except: e.append(i)
        elif incode:
            t = i.split()
            if not t:
                continue
            d.append(opcodes[t[0]])
            if len(t) > 1:
                d.append(t[1])
                if not opcodes[t[0]] in exempt:
                    a.append(tasm.index(l))
if last == 4 and len(e)%2 == 1:
    e.append(0)
out =""
print(e)
memoff = len(d)
for i in range(len(d)):
    if i%2==1:
        if not last in exempt:
            d[i] = int(d[i])+memoff-0
    
    last = d[i]

z=d+e
for i in z:
    out = out+str(i)+"\n"

with open("out.txt","w") as outf:
    outf.write(out)