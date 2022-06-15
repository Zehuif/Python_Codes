f = open("cincomil", "r")
f1 = open("cincomil1", "w")

rut = []
c=0
for x in f:
    x1 = x.replace(" ", "")
    line = x1.split("|")
    rut.append(line[0])
    if len(line[0])<=10 and len(line[1])<=50 and len(line[2])<=2 and len(line[3])<=101 and rut.count(rut[-1])==1:
        f1.write(x1)
    else:
        print(x1)

f1.close()
f.close()
