#Declarar Variables
antiguedad:int
bono:float
#Datos de entrada
antiguedad = int (input ('Ingresa el valor de antiguedad: '))
#Proceso
if antiguedad<=5:
    bono=antiguedad*100
else:
    bono=1000
    #Datos de salida
print ('Valor de bono: ' + repr (bono))