#Declarar Variables
dia_de_la_semana:int
#Datos de entrada
dia_de_la_semana = int (input ('Ingresa el valor de dia de la semana: '))
#Proceso
if dia_de_la_semana==1:
    print ('Lunes')
if dia_de_la_semana==2:
    print ('Martes')
if dia_de_la_semana==3:
    print ('Mircoles')
if dia_de_la_semana==4:
    print ('Jueves')
if dia_de_la_semana==5:
    print ('Viernes')
if dia_de_la_semana==6:
    print ('Sabado')
if dia_de_la_semana==7:
    print ('Domingo')
#Dato de salida   
print (dia_de_la_semana<1 or dia_de_la_semana>7)