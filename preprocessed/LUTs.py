andl = []
with open("and.txt","w") as andf:
    for i in range(256):
        for j in range(256):
            andl.append(i&j)
            print(256*256-i*j)
    out = ""
    for i in andl:
        out = out+str(i)+"\n"
    print("writeing")
    andf.write(out)
    print("wrote")
orl = []
with open("or.txt","w") as orf:
    for i in range(256):
        for j in range(256):
            orl.append(i|j)
            print(256*256-i*j)
    out = ""
    for i in orl:
        out = out+str(i)+"\n"
    orf.write(out)
xorl = []
with open("xor.txt","w") as xorf:
    for i in range(256):
        for j in range(256):
            xorl.append(i^j)
            print(256*256-i*j)
    out = ""
    for i in xorl:
        out = out+str(i)+"\n"
    xorf.write(out)
