class Nodo:
	def __init__(self, llave, pri, izq=None, der=None):
		self.llave=llave
		self.pri=pri
		self.izq=izq
		self.der=der
		self.padre=None

class Treap:
	def __init__(self):
		self.root=None

	def RotacionIzquierda(z):
		y=z.der
		T2=y.izq
		y.izq=z
		z.der=T2

		return y

	def RotacionDerecha(z):
		y=z.izq
		T3=y.der
		y.der=z
		z.izq=T3

		return y

	def Insertar(raiz, nodo):
		if raiz is None: 
			raiz = nodo
		else:
			if raiz.llave < nodo.llave:
				if raiz.der is None:
					raiz.der=Treap.Insertar(raiz.der, nodo)
					if raiz.der.pri > raiz.pri:
						raiz = Treap.RotacionIzquierda(raiz)
						print('Izquierda')
						return raiz
				else:
					Treap.Insertar(raiz.der, nodo)
					
			else:
				if raiz.izq is None:
					raiz.izq=Treap.Insertar(raiz.izq, nodo)
					if raiz.izq.pri > raiz.pri:
						raiz = Treap.RotacionDerecha(raiz)
						print('Derecha')
						return raiz
				else:
					Treap.Insertar(raiz.izq, nodo)
					
		return raiz
def inorder(root): 
    if root: 
        inorder(root.izq) 
        print(root.llave)
        print(root.pri)
        inorder(root.der)
        
N1=Nodo(50,73)
N2=Nodo(30,48)
N3=Nodo(20,92)
N4=Nodo(40,21)
N5=Nodo(70,50)
N6=Nodo(60,55)
N7=Nodo(80,44)

raiz=None
raiz=Treap.Insertar(raiz,N1)
raiz=Treap.Insertar(raiz,N2)
raiz=Treap.Insertar(raiz,N3)
raiz=Treap.Insertar(raiz,N4)
raiz=Treap.Insertar(raiz,N5)
raiz=Treap.Insertar(raiz,N6)
raiz=Treap.Insertar(raiz,N7)
inorder(raiz)
