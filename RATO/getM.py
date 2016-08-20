#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

def GetMouse(bt = 1, mod = 1, Pmax = 2000):

	import time
	import Gnuplot,sys, os.path
	
	#Funcao que converte de string para Hex
	def toHex(s):
	    lst = []
	    for ch in s:
		hv = hex(ord(ch)).replace('0x', '')
		if len(hv) == 1:
		    hv = '0'+hv
		lst.append(hv)
	    
	    return reduce(lambda x,y:x+y, lst)
	#---------------------------------------

	#Funcao que converte de Hex para inteiro
	def hex2int(s):
		return int(s, 16)

	f = open('/dev/input/mice','r')	#abre arquivo para leitura


	# digite o diretório onde vc quer salvar
	#----------------------------------------------------------------
	outdata = os.path.abspath('.') + '/data/outputDat.sil'
	sdata = open(outdata,'w')

	#----------------------------------------------------------------
	l=[]
	u = x = y = cc = bb= kk = aa = 0	#inicia contador,x e y
	t0 = time.time() 		#Pega o tempo inicial
	g=Gnuplot.Gnuplot()
	g('reset')
	g('set terminal x11')
	mode = mod
	mostra = bt
	while(u<Pmax):
	
		a = f.read(3)		#ler arquivo
		# aqui converte de string para Hex e de Hex para inteiro
		aa = hex2int('0x'+ toHex(a[0]))
		bb = hex2int('0x'+ toHex(a[1]))
		cc = hex2int('0x'+ toHex(a[2]))
		f.flush()
		#-------------------------------------------------------
		#Aqui corrigimos os valores para dar negativo com 0 no centro
		# = comentario
		if aa == 40:
			cc = (cc - 256) 
		if aa == 24:
			bb = (bb - 256.1)
		if aa == 56:
			bb = (bb - 256.1) 
			cc = (cc - 256)
		#-------------------------------------------------------	
		t = time.time() - t0
		x = x + bb 
		y = y + cc 
		
		if mode == 1:
			l.append([t,y])
			output =  str(t)+' '+str(y)+'\n'
		else:
			l.append([x,y])
			output =  str(x)+' '+str(y)+'\n'

		sdata.write(output)#escreve no arquivo

		if mostra == 1 and kk%40 == 0:
		   	g.plot(l)
		kk+=1
		u=u+1

	g.plot(l)
	time.sleep(3)	
	f.close()
	sdata.close()
	g=Gnuplot.Gnuplot()
	g('reset')
	g('set terminal x11')
	g('set data style dot')
	g('set terminal jpeg')
	Ano = time.localtime(time.time())[0]
	mes = time.localtime(time.time())[1]
	dia = time.localtime(time.time())[2]
	H = time.localtime(time.time())[3]
	M = time.localtime(time.time())[4]
	sg = time.localtime(time.time())[5]

	filenameImg = str(Ano)+str(mes)+str(dia)+str(H)+str(M)+str(sg)+'.jpg"'
	print filenameImg
	img = 'set output' + '"' +os.path.abspath('.') + '/data/'+ filenameImg
	g(img)
	plt = 'plot ' + '"' + outdata +'"' 
	g(plt)



versao = '0.1'




