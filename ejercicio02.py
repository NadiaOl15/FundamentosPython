print("Programa que calcula area y perimetro \n")

altura = input("Ingresa la altura: \n")
altura = int(altura)
base = int (input("Ingresa la base: \n"))

perimetro = base + altura + base + altura
area = base * altura

print ("El area del rectangulo es: " + str(area))
print ("El perimetro del rectangulo es: " + str(perimetro))