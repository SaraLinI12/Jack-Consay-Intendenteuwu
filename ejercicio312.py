#Declarar Varibles
horas_trabajadas:float
sueldo_semanal:int
pago_por_hora:float
#Datos de entrada
horas_trabajadas =float(input ('Ingresa el valor de horas trabajadas: '))
pago_por_hora =float(input ('Ingresa el valor de pago por hora: '))
sueldo_semanal=horas_trabajadas*pago_por_hora
#Proceso
if horas_trabajadas>40:
    sueldo_semanal=sueldo_semanal+(horas_trabajadas-40)*pago_por_hora
if horas_trabajadas>45:
    sueldo_semanal=sueldo_semanal+(horas_trabajadas-45)*pago_por_hora
if horas_trabajadas>50:
    sueldo_semanal=0
#Datos de salida
print ('Valor de sueldo semanal: ' + repr (sueldo_semanal))