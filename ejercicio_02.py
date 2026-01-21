ejercicio_02.py

#Calcular el parametro el perimetro y area de un rectangulo dada su base 

#Para realizar operaciones matematicas debemos convertir

print("Area y perimetro de un rectangulo")

base = input("Ingrse la base: ")
base = int(base)

altura = int(input("Ingrese la altura: "))

area = base * altura
perimetro = base * 2 + altura * 2

print("Area", area)
print("perimetro", perimetro)
 