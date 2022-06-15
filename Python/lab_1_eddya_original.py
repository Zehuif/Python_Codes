archivo=open('COVID19_open_line_list.csv', 'r')
lista = archivo.readlines()
numlin = 0
lista[numlin] = lista[numlin].replace(", ", " - ")
palabra = lista[numlin].split(",")
matriz = [[] for fila in range(len(palabra))]
for linea in lista:
    seguir = True
    lista[numlin]=lista[numlin].replace(", ", " - ")
    palabra=lista[numlin].split(",")
    ancho = len(palabra)
    for i in range(len(palabra)-1):
        if i < len(palabra):
            cont = 1
            if palabra[i].count('"') and palabra[i].count('"') == 1:
                while seguir:
                    palabra[i] = palabra[i] + ',' + palabra[i+1]
                    if palabra[i+1].count('"'):
                        seguir = False
                    palabra.pop(i + 1)
                    cont += 1
                i += cont
    numpal=0
    for i in palabra:
        matriz[numpal].append(i)
        numpal += 1
    numlin += 1  
archivo.close()

for i in range(len(matriz[0])):
    for j in range(len(matriz)):
        print(matriz[j][i])
