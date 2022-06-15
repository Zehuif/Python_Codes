def Frecuencia(text):
    Diccionario = dict()
    for i in range(len(text)):
        if text[i] in Diccionario:
            Diccionario[text[i]] += 1
        else:
            Diccionario[text[i]] = 1
    return Diccionario

class Nodo:
    def __init__(self, char, frecuencia, izq=None, dere=None):
        self.char = char
        self.frecuencia = frecuencia
        self.izq = izq
        self.dere = dere
        self.padre = None
        self.bit = None

def Arbol(Diccionario):
    Diccionario = sorted(Diccionario.items(), key=lambda value: value[1])
    nodos = list()
    for char, frecuencia in Diccionario:
        nodos.append(Nodo(char, frecuencia))

    while len(nodos) > 1:
        nodo1 = nodos[0]
        del nodos[0]
        nodo2 = nodos[0]
        del nodos[0]

        sum_frecuencia = nodo1.frecuencia + nodo2.frecuencia
        sum_char = nodo1.char + nodo2.char
        padre = Nodo(sum_char, sum_frecuencia, nodo1, nodo2)

        nodos.append(padre)
        nodos = sorted(nodos, key=lambda value: value.frecuencia)
    return padre

def get_Codigos(Nodo, bits, codigos=dict()):
    if len(Nodo.char) != 1:
        get_Codigos(Nodo.dere, bits + '1')
        get_Codigos(Nodo.izq, bits + '0')
    else:
        codigos[Nodo.char] = bits
    return codigos

def comprimir(text, codigos):
    binario = ''
    for c in text:
        binario+=codigos[c]
    print('Texto completo en binario:', binario)

text = input('Ingrese el texto a codificar:')
Diccionario = Frecuencia(text)
print('Frecuencias de caracteres:', Diccionario)
Arbol=Arbol(Diccionario)
Codigos = get_Codigos(Arbol, '')
print ('Codigo de cada caracter:', Codigos)
comprimir(text, Codigos)
