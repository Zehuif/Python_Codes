import random

n=0
for j in range (10):
    n+=10000
    for k in range (20):
        archivo=open('Datos1-'+str(j)+'-'+str(k)+'.txt','w')
        for i in range(0,n):
            archivo.write(str(random.randrange(1,10000)) + '\n')
        archivo.close

'''
Los Datos1-0-x son de 10.000 datos.
Los Datos1-1-x son de 20.000 datos.
Los Datos1-2-x son de 30.000 datos.
Los Datos1-3-x son de 40.000 datos.
Los Datos1-4-x son de 50.000 datos.
Los Datos1-5-x son de 60.000 datos.
Los Datos1-6-x son de 70.000 datos.
Los Datos1-7-x son de 80.000 datos.
Los Datos1-8-x son de 90.000 datos.
Los Datos1-9-x son de 100.000 datos.
Con numeros entre 1 y 10.000.
'''

n2=0
for j in range (5):
    n2+=1000000
    for k in range (20):
        archivo=open('Datos2-'+str(j)+'-'+str(k)+'.txt','w')
        for i in range(0,n2):
            archivo.write(str(random.randrange(1,100000)) + '\n')
        archivo.close
'''
Los Datos2-0-x son de 1.000.000 datos.
Los Datos2-1-x son de 2.000.000 datos.
Los Datos2-2-x son de 3.000.000 datos.
Los Datos2-3-x son de 4.000.000 datos.
Los Datos2-4-x son de 5.000.000 datos.
Los Datos2-5-x son de 6.000.000 datos.
Los Datos2-6-x son de 7.000.000 datos.
Los Datos2-7-x son de 8.000.000 datos.
Los Datos2-8-x son de 9.000.000 datos.
Los Datos2-9-x son de 10.000.000 datos.
Con numeros entre 1 y 100.000.
'''
