

def calcularMonedas(importe, sistemaMonetario):
	listaMonedas = []
	i = 0
	while importe != 0:

		while sistemaMonetario[i] > importe:
			i += 1

		listaMonedas.append(sistemaMonetario[i])
		importe = importe - sistemaMonetario[i]
		print(listaMonedas, importe, i)

	return listaMonedas


## Casos Test ##

sistemaMonetario = [500, 200, 100, 50, 20, 10, 5, 2, 1]

casosTest = [(123, [100, 20, 2, 1]),
			 (144, [100, 20, 20, 2, 2])
			]
importe = 2000
solucion = [500, 500, 500, 500]

listaMonedas = calcularMonedas(importe, sistemaMonetario)


longitudSolucion = len(listaMonedas)

fallo = False
i = 0
while i < longitudSolucion:
	if listaMonedas[i] != solucion[i]:
		fallo = True
		break
	else:
		i += 1

if fallo == True:
	print("Caso test FAIL %s" %(listaMonedas))
else:
	print("Caso test PASS %s" %(listaMonedas))