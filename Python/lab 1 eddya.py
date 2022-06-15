archivo = open('COVID19_open_line_list.csv', 'r')
lista = archivo.readlines()

numlin = 0
lista[numlin] = lista[numlin].replace(", ", " - ")
palabra = lista[numlin].split(",")
ancho = len(palabra)
matriz = [[] for fila in range(ancho)]
for linea in lista:
    ancho = len(palabra)
    palabra = lista[numlin].split(",")
    for cont in range(ancho - 1):
        seguir = False
        cadena =True
        print(cont)
        print('--------->', palabra[cont])
        if palabra[cont].find('"') == 0 or cadena:
            print('Encontrado')
            seguir = True
        while seguir:
            palabra[cont] = palabra[cont] + ',' + palabra[cont + 1]
            if palabra[cont].find('"') == -1:
                print('Parado')
                seguir = False
            print(palabra[cont])
            palabra.pop(cont + 1)
            ancho -= 1
    numpal = 0
    for i in palabra:
        print(i)
        matriz[numpal].append(i)
        numpal += 1
    numlin += 1
archivo.close()
for i in range(ancho):
    print(matriz[i][5378])
