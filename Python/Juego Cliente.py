import tkinter as tk
import time
#import winsound
from tkinter import messagebox as mb
from tkinter import *
from tkinter import ttk
from tkinter import font
import socket
import random
from  random import randrange
'''def conectar():
    global socket_cliente
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect(("192.168.137.1", 8000))
    print('Conectado')

#Cliente    
def enviar(mns):
    socket_cliente.send(mns.encode('utf-8'))
    return True

def recibir():
    global recibido
    recibido='0'
    recibido = socket_cliente.recv(1024)
    recibido=recibido.encode('utf-8')
    print (recibido)
    return True
    '''
def texto():
    archivo = open ('juego2.txt','r')
    mensaje = archivo.readline()
    x = mensaje.split()
    a=len(x)

    palabra=x[randrange(a)]

    return palabra
class Aplicacion:
    def __init__(self):
        """codigo para crear una ventana"""
        self.ventana=tk.Tk()
        self.ventana.title("Inhuman Reaction") #titulo de la ventana
        self.ventana.geometry("800x600") #dimensiones de la ventana
        self.ventana.configure(background='peru')
        self.Helvfont = font.Font(family="Helvetica", size=12, weight="bold")
        
        """"""

        """codigo para insertar una imagen"""
        #self.imagen=tk.PhotoImage(file="Captura.gif ")
        #self.fondo=tk.Label(self.ventana,image=self.imagen).place(x=0,y=0)

        """"""
        
        """esto es para ingresar un nombre de usuario y que en la ventana se agregue el nombre"""
        self.ventana.resizable(0,0) #con esto no agranda la ventana
        self.dato=tk.StringVar() 
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana, width=100, textvariable=self.dato)
        self.entry1.place(x=355, y=268, width=90, height=30)
        self.boton1=tk.Button(self.ventana, text="Ingrese nombre de usuario", command=self.ingresar)
        self.boton1.configure(bg='medium purple')
        self.boton1.configure(fg='black')
        self.boton1.place(x=310, y=300, width=180, height=30) 

        """"""
        self.ventana.mainloop()

        
    '''def sonido(self):
        winsound.PlaySound('reloj.wav',winsound.SND_FILENAME)
'''
    def ingresar(self):
        if self.dato.get()=='':
          mb.showinfo('Advertencia','No puedes dejar el cuadro de entrada vacia')
        else:
            self.ventana.title("Inhuman Reaction" + "-" + self.dato.get())
            self.boton1.destroy()
            self.entry1.destroy()
            self.boton2=tk.Button(self.ventana,text="Jugar",command=self.jugar)
            self.boton2.place(x=350, y=290, width=100, height=50)
            self.boton2.configure(bg="aquamarine4",fg='black')
            """
            self.instruccion=tk.Label(self.ventana,text="Instrucciones: aqui pondremos las instrucciones y luego de unos 10 segundos estas desaparaceran...")
            self.instruccion.place(x=250, y=190, width=200, height=200)
            self.instruccion.configure(bg='aquamarine4',fg='floral white')
            self.instruccion.after(10000, self.instruccion.destroy)
            """

    def jugar(self):
        #conectar()
        #cliente('listo')
        self.boton2.destroy()
        self.cp1=0
        self.cp2=0
        self.dato2=StringVar()
        self.dato2.set('hola')        #self.sonido()
        #self.sonido.after(10000,self.sonido.destroy)
        self.punto1=StringVar()
        self.punto1.set(0)
        self.punto2=StringVar()
        self.punto2.set(0)
        self.palabra=tk.Label(self.ventana,textvariable=self.dato2)

        self.palabra.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
        self.escribir=tk.Entry(self.ventana,width=130,textvariable=self.dato1)
        self.escribir.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)
        self.boton3=tk.Button(self.ventana,text='Evaluar',command=self.comparar)
        self.boton3.configure(bg='dim gray',fg='black')
        self.boton3.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)

        self.marcador1=tk.Label(self.ventana,textvariable=self.punto1)
        self.marcador1.place(x=250,y=400,width=90,height=90)
        self.marcador2=tk.Label(self.ventana,textvariable=self.punto2)
        self.marcador2.place(x=500,y=400,width=90,height=90)

    def comparar(self):
        if self.dato1.get() == self.dato2.get():
            self.cp1+=1
            self.mns=self.cp1
            self.mensaje=tk.Label(self.ventana,text='Correcto',bg='lime')
            self.escribir.delete(0,'end')
            self.mensaje.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
            self.mensaje.after(1000,self.mensaje.destroy)
            self.punto1.set(self.cp1)
            #recibir()
            #enviar(str(self.cp1))
            #self.cp2=recibido
            #self.punto2.set(self.cp2)
            if self.cp1==10:
                self.mensaje3=tk.Label(self.ventana,text='Ganaste',bg='yellow')
                self.mensaje3.pack(padx=10,pady=10,ipadx=10,ipady=10,fill=tk.X)
                self.mensaje3.after(4000,self.mensaje3.destroy)
                self.cp1=0
                self.punto1.set(0)
        else:
            self.mensaje2=tk.Label(self.ventana,text='Incorrecto',bg='red')
            self.escribir.delete(0,'end')
            self.mensaje2.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
            self.mensaje2.after(1000,self.mensaje2.destroy)
            #recibir()
            #enviar(str(self.cp1))
            #self.cp2=recibido
            #self.punto2.set(self.cp2)
        

        self.dato2.set(texto())

aplicacion1=Aplicacion()
