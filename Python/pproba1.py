import numpy as np
from scipy import stats

import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

f = open("TotalesNacionales_T.csv", 'r')
totals = []
for x in f:
    split = x.split(',')
    if split[0][0:7] == '2020-08':
        totals.append(split[7])

moda = stats.mode(totals)
print('La moda es {} con {} repeticiones.'.format(moda.mode[0], moda.count[0]))

np.median(totals)
