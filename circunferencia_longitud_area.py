import math

def Longitud(a):
    return math.pi * 2 * radio

def Area(a):
    return math.pi * radio**2  # area = math.pi * radio * radio  ;  area = math.pi * pow(radio,2)

print ('Introduce el radio de la circunferencia')
radio = input()
radio = int(radio)
print ('La longitud de la circunferencia es ', Longitud(radio))
print ('El area de la circunferencia es ', Area(radio))

