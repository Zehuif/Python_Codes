import random
from random import randrange
archivo = open ('juego2.txt','r')
mensaje = archivo.readline()
x = mensaje.split()
a=len(x)

palabra=x[randrange(a)]

return palabra
archivo.close()
