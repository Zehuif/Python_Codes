import csv
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


def main():
    with open('speedttest.csv') as archivo:
        reader = csv.reader(archivo, delimiter=";")
        tra = []
        band = []
        k = 0
        for row in reader:
            if k!=0:
                tra.append(float(row[1]))
                band.append(float(row[2]))
            #print("Intervalo[Sec]: {0}, Transferencia[Mbytes]: {1}, Bandwidth[Mbits]: {2}".format(row[0], row[1], row[2]))
            k=k+1
    archivo.close()
    tra.pop(0)
    band.pop(0)
    modab = stats.mode(band)
    modat = stats.mode(tra)
    print('BAND')
    print('La moda es {} con {} repeticion'.format(modab.mode[0], modab.count[0]))
    print('La mediana es', np.median(band))
    print('La media aritmetica es', np.mean(band))
    print('La desviacion standard es', np.std(band))
    print('La varianza es', np.var(band))

    print('BAND')
    print('La moda es {} con {} repeticion'.format(modat.mode[0], modab.count[0]))
    print('La mediana es', np.median(tra))
    print('La media aritmetica es', np.mean(tra))
    print('La desviacion standard es', np.std(tra))
    print('La varianza es', np.var(tra))

    plt.plot(band)
    plt.xlabel('Segundos')
    plt.ylabel('Ancho de banda')
    plt.title('Ancho de banda en intervalos de 1 segundos')
    plt.show()

    plt.plot(tra)
    plt.xlabel('Segundos')
    plt.ylabel('Ancho de banda')
    plt.title('Ancho de banda en intervalos de 1 segundos')
    plt.show()

    plt.hist(band)
    plt.xlabel('Bandwidth')
    plt.ylabel('Frecuencia')
    plt.title('Histograma Bandwidth')
    plt.show()


    # Graficando Normal
    mu, sigma = 166.2199016192317, 11.440604689628307  # media y desvio estandar
    normal = stats.norm(mu, sigma)
    x = np.linspace(50, 250, 100)
    fp = normal.pdf(band)  # Función de Probabilidad
    plt.plot(fp)
    plt.title('Distribución Normal')
    plt.ylabel('probabilidad')
    plt.xlabel('valores')
    plt.show()

    # Graficando Expotencial
    exponencial = stats.expon(166.2199016192317, 11.440604689628307)
    x = np.linspace(50, 250, 100)
    fp = exponencial.pdf(band)  # Función de Probabilidad
    plt.plot(x, exponencial.pdf(x))
    plt.title('Distribución Exponencial')
    plt.ylabel('probabilidad')
    plt.xlabel('valores')
    plt.show()

    # Graficando Uniforme
    uniforme = stats.uniform(166.2199016192317, 11.440604689628307)
    x = np.linspace(50, 250, 100)
    fp = uniforme.pdf(band)  # Función de Probabilidad
    plt.plot(x, uniforme.pdf(x))
    plt.title('Distribución Uniforme')
    plt.ylabel('probabilidad')
    plt.xlabel('valores')
    plt.show()

main()
