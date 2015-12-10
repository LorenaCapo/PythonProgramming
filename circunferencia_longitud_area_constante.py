PI = 3.1416
print ('Introduce el radio de la circunferencia')
radio = input()
radio = int(radio)
longitud = PI * 2 * radio
print ('La longitud de la circunferencia es ', longitud)
area = PI * radio**2  # area = PI * radio * radio  ;  area = PI * pow(radio,2)
print ('El area de la circunferencia es ', area)