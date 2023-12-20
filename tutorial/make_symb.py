import sys

fd_in = open(sys.argv[1],"r")
fd_out = open("symb.txt","w")

fd_out.write("<ctc> 0\n")

symbs = set()

for line in fd_in.readlines():
    aux = line.strip().split(" ")[1:]
    for s in aux:
        symbs.add(s)

i = 1
for s in list(symbs):
    fd_out.write(s+" "+str(i)+"\n")
    i += 1
