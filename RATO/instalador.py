#!/usr/bin/env python
#Organizar os arquivos nos seus respectivos lugares
#e checar se os modulos estao instalados corretamente
import os

print "checando modulos...\n"
try:
	import Gnuplot
except:
	print "Gnuplot e/ou modulo Python-GnuPlot nao instalado, deseja instalar agora[S:N]? "
	a = raw_input()
	if a == 'S'or a == 's':
		start = os.system
		print 'Instalando o GnuPlot...\n'
		start('sudo apt-get install gnuplot')
		print 'instalando a biblioteca python-gnuplot...\n'
		start('sudo apt-get install python-gnuplot')
	else:
		exit()

print "Modulos instalados\n"

UserPath = os.path.expanduser('~')
CriateDataPath = 'cd ' + UserPath +'\n' + 'mkdir RATO'
CriateDataPath2 = 'cd ' + UserPath +'/RATO\n' + 'mkdir data'
os.system(CriateDataPath)
os.system(CriateDataPath2)

DirPath = UserPath + '/RATO'

print 'Movendo os arquivos para a pasta ' + DirPath +'\n'
os.system('cp getM.py ' + DirPath)
os.system('cp StartRato.py ' + DirPath)
os.system('cp ico.png ' + DirPath)

print 'criando lancador...\n'
DirPathLanc = UserPath +'/Desktop/RATO.desktop'

File = open(DirPathLanc , 'w')

File.write('[Desktop Entry]\n')
File.write('Version=1.0\n')
File.write('Encoding=UTF-8\n')
File.write('Name=RATO\n')
File.write('Type=Application\n')
File.write('Terminal=false\n')
File.write('Icon[pt_BR]=gnome-panel-launcher\n')
File.write('Name[pt_BR]=RATO\n')
File.write('Exec=gksudo python ' + DirPath +'/StartRato.py\n')
File.write('Icon=' + DirPath + '/ico.png\n')
File.close()
print 'lancador criado na area de trabalho\n'

print 'Programa instalado e pronto para usar\n'
raw_input('ENTER\n')

