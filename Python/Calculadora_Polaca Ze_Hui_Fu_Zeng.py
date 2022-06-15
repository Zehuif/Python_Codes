import re
import sys
def Separar(ecuacion):
    ec=ecuacion.split()
    completo=[]
    while len(ec)!=0:
        if ec[0].isdigit()==False:
            if len(ec[0])>=2:
                ped=re.split('(\d+)',ec[0])
                while ped:
                    if ped.count(''):
                        ped.remove('')
                    while ped:
                        if len(ped)-1>0 and ped[0]=='-':
                            if ped[1].isdigit():
                                ped[0]=int(ped[0]+ped[1])
                                ped.pop(1)
                                completo.append(ped[0])
                                ped.pop(0)
                        elif ped[0].isdigit():
                            completo.append(int(ped[0]))
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
            completo.append(int(ec[0]))
            ec.pop(0)
    if completo.count('(')!=completo.count(')'):
            print('Operación mal definida 1.')
            sys.exit()
    if len(completo)>3:
        c=0
        for i in range(len(completo)):
            if type(completo[i])==int:
                c+=1
                if c>2:
                    print('Operación mal definida 2.')
                    sys.exit()
            else:
                c=0
    return completo

def CalcularPolaca(ecuacion):
    calculos=[]
    while ecuacion.count('('):
        ecuacion.pop(ecuacion.index('('))
    while ecuacion.count(')'):
        ecuacion.pop(ecuacion.index(')'))
    while ecuacion or len(calculos)!=1:
        if len(calculos)>=3:
            if type(calculos[-1])==int and type(calculos[-2])==int:
                if calculos[-3]=='*':
                    calculos[-3]=calculos[-2]*calculos[-1]
                    calculos.pop()
                    calculos.pop()
                elif calculos[-3]=='/':
                    calculos[-3]=int(calculos[-2]/calculos[-1])
                    calculos.pop()
                    calculos.pop()
                elif calculos[-3]=='-':
                    calculos[-3]=calculos[-2]-calculos[-1]
                    calculos.pop()
                    calculos.pop()
                elif calculos[-3]=='+':
                    calculos[-3]=calculos[-2]+calculos[-1]
                    calculos.pop()
                    calculos.pop()
            elif ecuacion:
                calculos.append(ecuacion[0])
                ecuacion.pop(0)
            else:
                print('Operación mal definida 4.')
                sys.exit()
        elif ecuacion:
            calculos.append(ecuacion[0])
            ecuacion.pop(0)
        else:
            print('Operación mal definida 3.')
            sys.exit()
    return int(calculos[0])

x=input('Ingrese la ecuacion: ')  
print(CalcularPolaca(Separar(x)))

