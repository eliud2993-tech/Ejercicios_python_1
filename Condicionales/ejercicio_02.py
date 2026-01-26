# Pedir un numero y decir si es positivo, negativo o 0
numero = int(input('Ingresa un numero:' ))

if numero == 0:
	print('El numero es cero')
else:
	if numero > 0:
		print('El numero es positivo')
	else:
		print('El numero es negativo')