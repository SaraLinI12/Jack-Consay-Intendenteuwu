#Datos de entrada
edad = int (input ('Ingresa el valor de edad: '))
#Proceso
print ('Selecciona el valor de sexo.')
print ('\t1.- mujer')
print ('\t2.- hombre')
sys.stdout.write ('\t')
sexo = 0
while sexo<1 or sexo>2:
    sexo = int (input (': '))
    if sexo<1 or sexo>2:
        sys.stdout.write ('Valor incorrecto. Ingresalo nuevamente.')
if (sexo==2 and edad>=16 and edad<70) or edad<16:
    print ('A')
if sexo==1 and edad>=16 and edad<70:
    print ('B')
if edad>70:
    print ('C')