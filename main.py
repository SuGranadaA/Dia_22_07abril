#Importamos la librería
from datetime import datetime, date, timedelta,time

#Leemos el archivo importado y creamos el archivo para la salida
fech1 = open('fecha1.txt','r')
calendar1 = open('calendario1.txt', 'w')

#Nombramos la lectura del archivo
leo1 = fech1.read()

#Cerramos el archivo
fech1.close()

#Imprimimos las fechas
calendar1.write(leo1)

#Abrimos el archivo de nuevo y procesamos los datos
fech1 = open('fecha1.txt','r')
leolista1 = fech1.readlines()

#Cerramos el archivo
fech1.close()

#Imprimimos los datos
print(leolista1)

#Transformamos los datos de fecha y los imprimimos
fe1 = (leolista1[0].rstrip())
fe2 = (leolista1[1].rstrip())
print(list(fe1))
print(list(fe2))

#Convertimos los datos a fechas
f1 = datetime.strptime(fe1,'%d/%m/%Y %H:%M:%S')
calendar1.write("\nFecha 1: ")
calendar1.write(str(f1))
f2 = datetime.strptime(fe2,'%d/%m/%Y %H:%M:%S')
calendar1.write("\nFecha 2: ")
calendar1.write(str(fe2))

#Realizamos modificaciones a las fechas
suma1 = (f1 + timedelta(weeks=27.5, days=3, hours=-20, minutes=550, seconds=24))
calendar1.write("\nModificamos la fecha 1: ")
calendar1.write(str(suma1))
print(suma1)
resta1 = (f2 - timedelta(weeks=10, days=1, hours=12, minutes=15, seconds=50))
calendar1.write("\nModificamos la fecha 2: ")
calendar1.write(str(resta1))
print(resta1)

#Comparamos dos fechas
comparacion1 = suma1>resta1
calendar1.write("\n¿La fecha 1 es mayor que la fecha 2?: ")
calendar1.write(str(comparacion1))

#Restamos las fechas anteriores
resta2 = f1-f2
calendar1.write("\nResta antigüa: ")
calendar1.write(str(resta2))

#Sumamos las nuevas fechas
suma2 = suma1+resta2
calendar1.write("\nSuma nueva: ")
calendar1.write(str(suma2))

#Identificamos los segundos contenidos en un tiempo
diezaños = timedelta(days=3650)
segundos = diezaños.total_seconds()
calendar1.write("\nSegundos en diez años: ")
calendar1.write(str(segundos))

#Cerramos el archivo
calendar1.close()


#Leemos el archivo importado y creamos el archivo para la salida
fech2 = open('fecha2.txt','r')
calendar2 = open('calendario2.tx', 'w')

#Nombramos la lectura del archivo
leo2 = fech2.read()

#Cerramos el archivo
fech2.close()

#Imprimimos las fechas
calendar2.write(leo2)

#Abrimos el archivo de nuevo y procesamos los datos
fech2 = open('fecha2.txt','r')
leolista2 = fech2.readlines()

#Cerramos el archivo
fech2.close()

#Imprimimos los datos
print((leolista2))

#Transformamos los datos de fecha y los imprimimos
fechita1 = (leolista2[0].rstrip())
fechita2 = (leolista2[1].rstrip())
print(fechita1)
print(fechita2)

#Convertimos los datos a enteros y los imprimimos
añofechita1= int(fechita1[1:5])
print(añofechita1)
mesfechita1= int(fechita1[6:8])
print(mesfechita1)
diafechita1= int(fechita1[9:11])
print(diafechita1)
añofechita2= int(fechita2[1:5])
print(añofechita2)
mesfechita2= int(fechita2[6:8])
print(mesfechita2)
diafechita2= int(fechita2[9:11])
print(diafechita1)

#Modificamos las fechas
fech1 = date(añofechita1,mesfechita1,diafechita1)
actualizamos1 = fech1 + timedelta(days=3,weeks=2)
calendar2.write("\nFecha 1 original: ")
calendar2.write(str(fech1))
calendar2.write("\nFecha 1 modificada: ")
calendar2.write(str(actualizamos1))
print(fech1)
print(actualizamos1)
fech2 = date(añofechita2,mesfechita2,diafechita2)
actualizamos2 = fech2 + timedelta(days=-7,weeks=-4)
calendar2.write("\nFecha 2 original: ")
calendar2.write(str(fech2))
calendar2.write("\nFecha 2 modificada: ")
calendar2.write(str(actualizamos2))
print(fech2)
print(actualizamos2)

#Identificamos el objeto mínimo y máximo
minimo = timedelta.min
print(minimo)
calendar2.write("\nMínimo: ")
calendar2.write(str(minimo))
maximo = timedelta.max
print(maximo)
calendar2.write("\nMáximo: ")
calendar2.write(str(maximo))

#Cerramos el archivo
calendar2.close()