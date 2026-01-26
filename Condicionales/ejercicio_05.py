# Programa que valide usuario y contraseña

user = 'admin'
password = 'qwerty'

usuario = input('Ingresa tu usuario: ')
contra = input('Ingresa tu contraseña: ')

if user == usuario and password == contra:
	print('Has entrada al sistema')
else:
	print('Error de acceso')
	