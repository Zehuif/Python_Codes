import re
import sys
calcular=[]
completo=[]
pa2=[]
num=[]
j=0
def polaca(ecuacion):
    co=0
    ec=ecuacion.split()
    if ecuacion.count('(')!=ecuacion.count(')'):
        print('Operación mal definida.')
        sys.exit()
    while len(ec)!=0:
        print('completo', completo)
        if ec[0].isdigit()==False:
            if len(ec[0])>=2:
                ped=re.split('(\d+)',ec[0])
                print('ped',ped)
                while ped:
                    if ped.count(''):
                        ped.remove('')
                    while ped:
                        print('ped1',ped)
                        if len(ped)-1>0 and ped[0]=='-':
                            print('ped2',ped)
                            if ped[1].isdigit():
                                ped[0]=ped[0]+ped[1]
                                ped.pop(1)
                                print('ped3',ped)
                                completo.append(ped[0])
                                ped.pop(0)
                        elif ped[0].isdigit():
                            completo.append(ped[0])
                            ped.pop(0)
                        else:
                            for c in ped[0]:
                                completo.append(c)
                            ped.pop(0)
                ec.pop(0)
            else:
                completo.append(ec[0])
                ec.pop(0)
        else:
            completo.append(ec[0])
            ec.pop(0)
    return completo

def parentesis(completo):
    c=0
    pa=[]
    global j
    while len(completo)!=0:
        if completo[0]=='(':
            completo.pop(0)
            c+=1
            while c!=0:
                if completo[0]=='(':
                    pa.append(completo[0])
                    completo.pop(0)
                    c+=1
                elif completo[0]==')':
                    pa.append(completo[0])
                    completo.pop(0)
                    c-=1
                else:
                    pa.append(completo[0])
                    completo.pop(0)
            pa.pop()
            if pa.count('(')!=0:
                parentesis(pa)
            if len(pa)!=0:
                calculo(pa)
            if len(completo)!=0:
                parentesis(completo)
        else:
            print (completo)
            if len(completo)>2:
                if completo[1]=='(':
                    j+=1
            if j>1:
                pa2.append(completo[0])
                completo.pop(0)
            else:
                print('completo',completo)
                calcular.append(completo[0])
                completo.pop(0)
                print('calcula',calcular)
            if len(calcular)>=3:
                print('calcular ult',calcular)
                calculo(calcular)
            
def calculo(pa):
    global j
    print('pa',pa)
    if pa[0]!='+' and pa[0]!='-' and pa[0]!='*' and pa[0]!='/':
        print('Operación mal definida.')
        sys.exit()
    if pa[0]=='*':
        val=int(pa[1])*int(pa[2])
    elif pa[0]=='/':
        val=int(pa[1])/int(pa[2])
    elif pa[0]=='-':
        val=int(pa[1])-int(pa[2])
    elif pa[0]=='+':
        val=int(pa[1])+int(pa[2])
    pa.clear()
    if j>1:
        pa2.append(val)
        if len(pa2)==3:
            j=1
            print('pa2',pa2)
            calculo(pa2)
    else:
        calcular.append(val)
    if len(calcular)==3:
        calculo(calcular)
        print ('calcular superult', calcular)
    return calcular

   
x=input('Ingrese ecuación con notación polaca correctamente escrita: ')
print(x)
parentesis(polaca(x))
print(calcular[0])

