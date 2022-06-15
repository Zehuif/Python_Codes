import time

def BubbleSort(arreglo):
    for i in range(len(arreglo)):
         for j in range(0, len(arreglo)-i-1):
            if arreglo[j] > arreglo[j+1] :
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

def InsertionSort(arreglo): 
    for i in range(1, len(arreglo)): 
        mini = arreglo[i]  
        j = i-1
        while j >=0 and mini < arreglo[j] : 
                arreglo[j+1] = arreglo[j] 
                j -= 1
        arreglo[j+1] = mini 

def SelectionSort(arreglo):
    for i in range(len(arreglo)): 
        mini_idx = i 
        for j in range(i+1, len(arreglo)):
            if arreglo[mini_idx] > arreglo[j]:
                mini_idx = j     
        arreglo[i], arreglo[mini_idx] = arreglo[mini_idx], arreglo[i] 

def MergeSort(arreglo): 
    if len(arreglo) >1: 
        mid = len(arreglo)//2 
        L = arreglo[:mid] 
        R = arreglo[mid:] 
        MergeSort(L) 
        MergeSort(R) 
        i = j = k = 0

        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arreglo[k] = L[i] 
                i+=1
            else: 
                arreglo[k] = R[j] 
                j+=1
            k+=1
          
        while i < len(L): 
            arreglo[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arreglo[k] = R[j] 
            j+=1
            k+=1

def partition(arreglo,menor,mayor): 
    i = ( menor-1 )
    pivote = arreglo[mayor] 
  
    for j in range(menor , mayor):
        if   arreglo[j] <= pivote:
            i = i+1 
            arreglo[i],arreglo[j] = arreglo[j],arreglo[i] 
    arreglo[i+1],arreglo[mayor] = arreglo[mayor],arreglo[i+1] 
    return ( i+1 ) 

def _QuickSort(arreglo,menor,mayor): 
    if menor < mayor: 
        pi = partition(arreglo,menor,mayor) 
        _QuickSort(arreglo, menor, pi-1) 
        _QuickSort(arreglo, pi+1, mayor)

def QuickSort(arreglo):
	_QuickSort(arreglo,0,len(arreglo)-1)

def CountingSort(arreglo):
    c = [0]*( max(arreglo) + 1)

    for i in range(len(arreglo)):
        c[arreglo[i]] = c[arreglo[i]] + 1
    c[0] = c[0] - 1 

    for i in range(1, max(arreglo) + 1):
        c[i] = c[i] + c[i - 1]
    ordenado = [None]*len(arreglo)

    for x in arreglo:
        ordenado[c[x]] = x
        c[x] = c[x] - 1
    return ordenado

sort=['BubbleSort','InsertionSort','SelectionSort','MergeSort',
'QuickSort','CountingSort']
s=5
if sort[s]=='BubbleSort' or sort[s]=='InsertionSort' or sort[s]=='SelectionSort':
	l=1
else:
	l=2
archivot=open(sort[s]+'.txt','w')
archivot.write(sort[s] + '\n')
archivot.close
for i in range(10):
    print(i)
    archivot=open(sort[s]+'.txt','a')
    archivot.write(sort[s]+' '+ str(i) + '\n')
    archivot.close
    for j in range(20):
        print(j)
        archivo=open('Datos'+str(l)+'-'+str(i)+'-'+str(j)+'.txt','r')
        lista=archivo.read()
        archivo.close
        lista=lista.split('\n')
        lista.pop()
        lista = [int(k) for k in lista]
        time1= time.time()
        if sort[s]=='BubbleSort':
            BubbleSort(lista)
        elif sort[s]=='InsertionSort':
            InsertionSort(lista)
        elif sort[s]=='SelectionSort':
            SelectionSort(lista)
        elif sort[s]=='MergeSort':
            MergeSort(lista)
        elif sort[s]=='QuickSort':
            QuickSort(lista)
        elif sort[s]=='CountingSort':
            CountingSort(lista)
        time2= time.time()
        time1=time2-time1
        archivot=open(sort[s]+'.txt','a')
        archivot.write(str(time1) + '\n')
        archivot.close



