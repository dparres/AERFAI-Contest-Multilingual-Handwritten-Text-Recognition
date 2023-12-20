import sys

text = open(sys.argv[1], "r").readlines()
text_out = open(sys.argv[2],"w")

for line in text:
    aux = line.strip().split(" ")
    id = aux[0]
    line_text = aux[1:]
    text_out.write(id + " ")
    for tok in line_text:
        for char in tok:
            text_out.write(char + " ")
        
        text_out.write("<space> ")
    text_out.write("\n")

