from scipy.stats import hypergeom
import matplotlib.pyplot as plt
import numpy as np

N, d, n = 10, 7, 3

hipergeometrica = hypergeom(N,d,n)

x = np.arange(0,n+1)

y = hipergeometrica.pmf(x)

#Estadigrafos
print( "E(X) = ",n*d/N)
print ("var(x) = ",(((N-n)/(N-1))*(n*d/N))*(1-(d/N)))

#Variables
print("X",x)
print("Y",y)


#Generar 100000 muestra

Rand = hypergeom.rvs(N,d,n,size = 10000)
print (Rand)
print("E(Rand)",np.mean(Rand))
print ("V(Rand",np.var(Rand))

plt.plot(x,y, "--")
plt.vlines(x,0,y, colors= "b",lw=5,alpha=0.5)
plt.title("Distribucion Hipergeometrica")
plt.ylabel('Probabilidad')
plt.xlabel('Valores')
plt.show()