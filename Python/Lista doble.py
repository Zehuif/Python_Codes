class nodo(object):
    def __init__(self, _value):
        self.pSig=None
        self.pAnt=None
        self.value=_value

    def getElemento(delf):
        return self.value

class listaDoble(object):
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def getVacio(self):
        if self.primero==None:
            return True

    def printPrimeroUltimo(self):
        if self.getVacio()==True:
            print ('Esta vacia la lista')
        else:
            validar=True
            temp=self.primero
            while(validar):
                print(temp.getElemento())
                if temp==self.ultimo:
                    validar=False
                else:
                    temp=temp.pSig

    def printUltimoPrimero(self):
        if self.getVacio()==True:
            print('Esta vacia la lista')
        else:
            validar=True
            temp=self.ultimo
            while (validar):
                print(temp.getValor)
                if temp==self.primero:
                    validar=False
                else:
                    temp=temp.pAnt

    def EliminarPrimero(self):
        if self.getVacio()==True:
            print ('La lista ya esta vacia')
        elif self.primero==self.ultimo:
            self.primero=self.ultimo=None
            print ('La lista esta vacia')
        else:
            temp=self.primero
            self.primero=temp.pSig
            self.primero.pAnt=None
            temp=None








    
