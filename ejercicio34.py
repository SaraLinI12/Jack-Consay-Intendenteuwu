   #Declarar Variables
tarifa:float
horas:int
cobro:float
   #Datos de Entrada
tarifa=int(input("Ingrese el costo por hora"))
horas=int(input("Ingrese la cantidad de horas"))
   #Proceso
if horas<=2:
    cobro=horas*5
if horas>2 and horas<=5:
    cobro=2*5+(horas-2)*4
if horas>5 and horas<=10:
    cobro=2*5+3*4+(horas-5)*3
if horas>10:
    cobro=2*5+3*4+3*5+(horas-10)*2


