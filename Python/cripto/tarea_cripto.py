import codecs
import numpy as np


def getData(): 
    palabra = ''
    data = []
    df = open("cripto.txt")
    lineas = df.readlines()
    for linea in lineas:
        for char in linea:
            if(char=='\n'):
                continue
            else:
                palabra = palabra + char
        data.append(palabra)
        break
    data.append(lineas.pop())
    return data

def matrix(llave):
    print('La llave es: ', llave)
    hex = llave.encode('ascii').hex()
    print('La llave en hex: ', hex)
    universo = '0123456789abcdef'
    matris =np.zeros(16, dtype='S')
    count = 0
    for i in hex:
        if(np.where(matris == i.encode())[0].size == 0):
            matris[count] = i
            count+=1
    for i in universo:
        if(np.where(matris == i.encode())[0].size == 0):
            matris[count] = i
            count+=1
    matris = matris.reshape(4,4)
    print('La matris es:\n', matris)
    return matris

def cifrar(matris, mensaje):
    print('El mensaje es: ',mensaje)
    matris2 = matris
    matris2 = np.insert(matris2, 4, matris[:,0], axis=1)
    matris2 = np.insert(matris2, 0, matris[:,3], axis=1)
    matris2 = np.insert(matris2, 0, matris2[3], axis=0)
    matris2 = np.insert(matris2, 5, matris2[1], axis=0)
    matris2 = matris2.reshape(36)
    matris = matris.reshape(16)    
    mensaje = mensaje.encode('ascii').hex()
    cifrado = ''
    print('Mensaje en hex: ',mensaje)
    for i in range(0,len(mensaje),+2):
        columna = False
        fila = False
        posicion11 = np.where(matris == mensaje[i].encode())[0][0]
        posicion1 = posicion11 + 7 + 2 * int(posicion11/4)
        posicion22 = np.where(matris == mensaje[i+1].encode())[0][0]
        posicion2 = posicion22 + 7 + 2 * int(posicion22/4)
        if(posicion11%4 == posicion22%4):
            columna = True
        if(int(posicion11/4) == int(posicion22/4)):
            fila = True
        if(columna == False and fila == False):
            posicion1 = posicion1 + 29
            posicion2 = posicion2 + 7
            if(posicion1 >= 36):
                posicion1 -= 36
            if(posicion2 >= 36):
                posicion2 -=36
        elif(columna == False and fila == True):
            posicion1 = posicion1 + 30
            posicion2 = posicion2 + 6
            if(posicion1 >= 36):
                posicion1 -= 36
            if(posicion2 >= 36):
                posicion2 -=36
        elif(columna == True and fila == False):
            posicion1 = posicion1 + 35
            posicion2 = posicion2 + 1
            if(posicion1 >= 36):
                posicion1 -= 36
            if(posicion2 >= 36):
                posicion2 -=36
        cifrado = cifrado + matris2[posicion1].decode() + matris2[posicion2].decode()
    print('Codificado: ',cifrado)
    return cifrado

def descifrar(llave, cifrado):
    matris = matrix(llave)
    print('El cifrado es: ',cifrado)
    matris2 = matris
    matris2 = np.insert(matris2, 4, matris[:,0], axis=1)
    matris2 = np.insert(matris2, 0, matris[:,3], axis=1)
    matris2 = np.insert(matris2, 0, matris2[3], axis=0)
    matris2 = np.insert(matris2, 5, matris2[1], axis=0)
    matris2 = matris2.reshape(36)
    matris = matris.reshape(16)
    mensaje = ''
    print('cifrado en hex: ',cifrado)
    for i in range(0,len(cifrado),+2):
        columna = False
        fila = False
        posicion11 = np.where(matris == cifrado[i].encode())[0][0]
        posicion1 = posicion11 + 7 + 2 * int(posicion11/4)
        posicion22 = np.where(matris == cifrado[i+1].encode())[0][0]
        posicion2 = posicion22 + 7 + 2 * int(posicion22/4)
        if(posicion11%4 == posicion22%4):
            columna = True
        if(int(posicion11/4) == int(posicion22/4)):
            fila = True
        if(columna == False and fila == False):
            posicion1 = posicion1 + 29
            posicion2 = posicion2 + 7
            if(posicion1 >= 36):
                posicion1 -= 36
            if(posicion2 >= 36):
                posicion2 -=36
        elif(columna == False and fila == True):
            posicion1 = posicion1 + 30
            posicion2 = posicion2 + 6
            if(posicion1 >= 36):
                posicion1 -= 36
            if(posicion2 >= 36):
                posicion2 -=36
        elif(columna == True and fila == False):
            posicion1 = posicion1 + 35
            posicion2 = posicion2 + 1
            if(posicion1 >= 36):
                posicion1 -= 36
            if(posicion2 >= 36):
                posicion2 -=36
        mensaje = mensaje + matris2[posicion1].decode() + matris2[posicion2].decode()
    print('Codificado: ',cifrado)
    return cifrado

def main():
    data = getData()
    matris = matrix(data[0])
    cifrado = cifrar(matris, data[1])
    #mensaje = descifrar(data[0], cifrado)

main()