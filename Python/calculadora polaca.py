operadores=[]
numeros=[]
resultado=[]

def polaca(ecuacion):
    ec=ecuacion.split()
    while len(ec)!=0:
        if ec[0].isdigit()==False:
            for c in ec[0]:
                if c.isdigit():
                    numeros.append(c)
                else:
                    operadores.append(c)
            ec.pop(0)
        elif ec[0].isdigit():
            numeros.append(ec[0])
            ec.pop(0)
        else:
            operadores.append(ec[0])
            ec.pop(0)
        
    print(operadores)
    print(numeros)
    return resultado


    

print(polaca('- (* 3 4) (/ 10 -5)'))
