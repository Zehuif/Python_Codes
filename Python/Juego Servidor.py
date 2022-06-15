import tkinter as tk
import time
import winsound
import socket
from tkinter import messagebox as mb
from tkinter import *
from tkinter import ttk
from tkinter import font
import random
from random import randrange

def conectado():
    global s
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("192.168.137.1",8000))
    s.listen(5)
    print('conectado')
    print ("Esperando conexión...")
    global sc
    global addr
    sc, addr= s.accept()
    print ("Cliente conectado desde: ", addr)
    

def recibir():
    global recibido
    recibido=sc.recv(1024)
    recibido=recibido.decode('utf-8')
    return (True)

def enviar(msn):
    sc.send(msn.encode('utf-8'))
            #s.send(msn.encode('utf-8'))
    
    
#servidor()
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
        self.ventana.configure(background='PeachPuff3')
        
        """"""

        """codigo para insertar una imagen"""
        #self.imagen=tk.PhotoImage(file="Captura.gif ")
        #self.fondo=tk.Label(self.ventana,image=self.imagen).place(x=0,y=0)

        """"""
        
        """esto es para ingresar un nombre de usuario y que en la ventana se agregue el nombre"""
        self.ventana.resizable(0,0) #con esto no agranda la ventana
        self.dato=tk.StringVar() 
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana, width=110, textvariable=self.dato)
        self.entry1.configure(font='helvetica 12')
        self.entry1.place(x=335, y=238, width=130, height=50)
        self.boton1=tk.Button(self.ventana, text="Ingrese nombre de usuario", command=self.ingresar)
        self.boton1.configure(bg='slate blue')
        self.boton1.configure(fg='ghost white')
        self.boton1.place(x=320, y=300, width=160, height=30) 

        """"""
        self.ventana.mainloop()

    #def sonido(self):
    #winsound.PlaySound('reloj.wav',winsound.SND_FILENAME)

    def ingresar(self):
        if self.dato.get()=='':
          mb.showinfo('Advertencia','No puedes dejar el cuadro de entrada vacia')
        else:
            self.ventana.title("Inhuman Reaction" + "-" + self.dato.get())
            self.boton1.destroy()
            self.entry1.destroy()
            self.boton2=tk.Button(self.ventana,text="Jugar",command=self.jugar)
            self.boton2.place(x=350, y=290, width=100, height=50)
            self.boton2.configure(bg="aquamarine4",fg='floral white')
            """
            self.instruccion=tk.Label(self.ventana,text="Instrucciones: aqui pondremos las instrucciones y luego de unos 10 segundos estas desaparaceran...")
            self.instruccion.place(x=250, y=190, width=200, height=200)
            self.instruccion.configure(bg='aquamarine4',fg='floral white')
            self.instruccion.after(10000, self.instruccion.destroy)
            """

    def jugar(self):
        conectado()
        self.boton2.destroy()
        #print (servidor('listo'))
        self.dato2=tk.StringVar()
        self.dato2.set(texto())
        self.cp1=0
        self.cp2=0
        self.punto1=StringVar()
        self.punto2=StringVar()
        self.punto1.set(0)
        self.punto2.set(0)
        self.palabra=tk.Label(self.ventana,textvariable=self.dato2)
        self.palabra.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
        self.escribir=tk.Entry(self.ventana,width=130,textvariable=self.dato1)
        self.escribir.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)
        self.boton3=tk.Button(self.ventana,text='evaluar',command=self.comparar)
        self.boton3.configure(bg='dim gray',fg='azure')
        self.boton3.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
        self.marcador1=tk.Label(self.ventana,textvariable=self.punto1)
        self.marcador1.place(x=250,y=400,width=90,height=90)
        self.marcador2=tk.Label(self.ventana,textvariable=self.punto2)
        self.marcador2.place(x=500,y=400,width=90,height=90)
        
    def comparar(self):
        self.dato2.set(texto())
        if self.dato1.get() == self.dato2:
            self.cp1+=1
            self.mensaje=tk.Label(self.ventana,text='correcto')
            self.escribir.delete(0,'end')
            self.mensaje.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
            self.mensaje.after(1000,self.mensaje.destroy)
            self.punto1.set(self.cp1)
            enviar(str(self.cp1))
            recibir()
            self.cp2=recibido
            self.punto2.set(self.cp2)

        else:
            self.mensaje2=tk.Label(self.ventana,text='incorrecto')
            self.escribir.delete(0,'end')
            self.mensaje2.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
            self.mensaje2.after(1000,self.mensaje2.destroy)
            enviar(str(self.cp1))
            recibir()
            self.cp2=recibido
            self.punto2.set(self.cp2)

        if self.dato1==10:
            self.mensaje3=tk.Label(self.ventana,text='Ganaste')
            self.mensaje3.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)


archivo.close()
aplicacion1=Aplicacion()




