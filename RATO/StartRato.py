#!/usr/bin/python

from Tkinter import *
from ctypes import *
import time, math, os, Gnuplot, getM

#-------------------------------^^^^^^^^^^^^^^^^^^^^^^^^------------------------------

class Griding:
    def __init__(self,raiz):
        self.raiz = raiz
        self.raiz.title('Rato!')
	self.raiz.resizable(width = False, height = False)

	#variaveis do programa----------------------------------------------------------------------------------------------
	self.CheckButtonVar = IntVar()
	self.CheckButtonVar2 = IntVar()
	self.CheckButtonVar3 = IntVar()
	self.pontos = IntVar()

	#--------------Frame_LOG-------------------------
	self.frame = Frame(self.raiz, width=410, height=500)
	self.frame.grid(row=3, column=1, columnspan = 3, padx=3, pady=3)

	#--------------LOG texto-------------------------
	self.msgTitle=Label(self.frame,text='LOG --------------------------------------------------------------------------')
        self.msgTitle.grid(row=1, column=1,columnspan = 3)

	self.msg1=Label(self.frame,text='Grafico - OFF')
        self.msg1.grid(row=2, column=1,columnspan = 3)

	self.msg2=Label(self.frame,text='Aguardando captura')
        self.msg2.grid(row=3, column=1,columnspan = 3)

	self.msg3=Label(self.frame,text='Modo de captura: Y x T')
        self.msg3.grid(row=4, column=1,columnspan = 3)


	#---------------CheckButton-----------------------
	CB = Checkbutton(self.raiz, text = "Mostrar grafico  ",  variable = self.CheckButtonVar, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 20, command=self.LOG).grid(row=1, column=2, sticky=W, padx=3, pady=3)

	CB2 = Checkbutton(self.raiz, text = "Modo de Captura  ",  variable = self.CheckButtonVar2, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 20, command=self.conf).grid(row=1, column=1, sticky=W, padx=3, pady=3)

	CB3 = Checkbutton(self.raiz, text = "Mostrar pasta  ",  variable = self.CheckButtonVar3, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 20, command=self.conf).grid(row=1, column=3, sticky=W, padx=3, pady=3)

	#---------------Botoes----------------------------
        self.ini=Button(self.raiz, width=12, command=self.inicia, text='Iniciar')
	self.ini.bind("<Enter>", self.LOG_b)
        self.ini.grid(row=2, column=3, padx=3, pady=3)

	self.msg4=Label(self.raiz,text='Numero de pontos:')
        self.msg4.grid(row=2, column=1)

	self.Pmaximo=Entry(self.raiz, width=20)
        self.Pmaximo.grid(row=2, column=2, padx=3, pady=3)

	#self.salv=Button(self.raiz, width=12, command=self.salva, text='Salvar valor')
        #self.salv.grid(row=2, column=3, padx=3, pady=3)
	#-------------------------------------------------
	
  
    def conf(self):
	if self.CheckButtonVar2.get() == 1: 
		self.msg3['text'] = 'Modo de Captura: Y x T'
	else: 
		self.msg3['text'] = 'Modo de Captura: X x Y'

    def LOG(self):
	if self.CheckButtonVar.get() == 1: 
		self.msg1['text'] = 'Grafico - ON'
	else: 
		self.msg1['text'] = 'Grafico - OFF'

    def LOG_b(self, event):
        self.msg2['text'] = 'Aguardando captura'
#-------------------------------------------------------------------Obtencao dos dados------------------
    def inicia(self):
	ckb = self.CheckButtonVar.get()
	ckb2 = self.CheckButtonVar2.get()

	try:
		self.pontos = int(self.Pmaximo.get())
	except:
		self.pontos = 1000
	if self.pontos <= 1: 
		self.pontos = 1000

	getM.GetMouse(ckb, ckb2, self.pontos)
	
	if self.CheckButtonVar3.get() == 1:
		#-------------------------------------Mostra pasta
		UserPath = os.path.abspath('.') + '/RATO/data'
		os.system('nautilus ' + UserPath)
		#-------------------------------------

	self.msg2['text'] = 'Captura terminada'

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^Obtencao dos dados------------------

main=Tk()
Griding(main)
main.mainloop()

