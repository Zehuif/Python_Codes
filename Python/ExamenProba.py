import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import math

f = open("dataSet09.csv", 'r')
tiempos = []
for x in f:
    tiempos.append(float(x))
moda = stats.mode(tiempos)
print('La moda es {} con {} repeticiones'.format(moda.mode[0], moda.count[0]))
print('La mediana es', np.median(tiempos))
print('La media aritmetica es', np.mean(tiempos))
print('La desviacion standard es', np.std(tiempos))
print('La varianza es', np.var(tiempos))

# Grafico

plt.plot(tiempos)
plt.xlabel('Numero de prueba')
plt.ylabel('Tiempo de ejecucion')
plt.title('Tiempo de ejecucion de algoritmo de Fibonacci entre los valores 30 y 40')
plt.show()

# Histograma

n, bins, patches = plt.hist(x=tiempos, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Tiempos')
plt.ylabel('Frecuencia')
plt.title('Histograma')
plt.show()




# Normal

normal = stats.norm(np.mean(tiempos), np.std(tiempos))
fp = normal.pdf(tiempos)  # Función de Probabilidad
plt.plot(fp)
plt.title('Distribución Normal')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()

# Expotencial

exponencial = stats.expon(np.mean(tiempos), np.std(tiempos))
fp = exponencial.pdf(tiempos)  # Función de Probabilidad
plt.plot(fp)
plt.title('Distribución Exponencial')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()

# Uniforme

uniforme = stats.uniform(np.mean(tiempos), np.std(tiempos))
fp = uniforme.pdf(tiempos)  # Función de Probabilidad
plt.plot(fp)
plt.title('Distribución Uniforme')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()

# Poisson
min = 10000
max = 0
for t in tiempos:
    if min > t:
        min = t
    if max < t:
        max = t
print(min, max)
poisson = stats.poisson(np.mean(tiempos)) # Distribución
x = np.arange(poisson.ppf(min),
              poisson.ppf(max))
fmp = poisson.pmf(x) # Función de Masa de Probabilidad
plt.plot(x, fmp, '--')
plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
plt.title('Distribución Poisson')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()