################################################################################
#si el segundo no es cero, o un mensaje de aviso en caso contrario.
#Crea un programa que pida al usuario dos números y muestre su división 
################################################################################

numero1 = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa otro numero: "))

if numero2 !=0:
    division = numero1 / numero2
    print(numero1, "entre", numero2, " es igual a: ", division)

else:
    print("No se puede dividir entre 0")
