import numpy as np
from scipy import stats

import matplotlib.pyplot as plt

f = open("TotalesNacionales_T.csv", 'r')
totals = []
for x in f:
    split = x.split(',')
    if split[0][0:7] == '2020-08':
        totals.append(float(split[7]))

moda = stats.mode(totals)
print('La moda es {} con {} repeticion'.format(moda.mode[0], moda.count[0]))
print('La mediana es', np.median(totals))
print('La media aritmetica es', np.mean(totals))
print('La desviacion standard es', np.std(totals))
print('La varianza es', np.var(totals))


n, bins, patches = plt.hist(x=totals, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Contagiados')
plt.ylabel('Frecuencia')
plt.title('Histograma de casos Agosto Chile')
plt.text(23, 45, r'$\mu=15, b=3$')
plt.show()

plt.plot(totals)
plt.xlabel('Dias del mes')
plt.ylabel('Contagiados')
plt.title('Grafico de casos Agosto Chile')
plt.show()
