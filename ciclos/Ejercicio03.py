################################################################################
#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma
#y la media de todos los números introducidos.
################################################################################

suma = 0
numeros = 0
while True:
    numero = int(input('Ingresa un numero: '))
    if numero == 0:
        print('La suma de los numeros ingresados es:', suma)
        print('La media de los numeros ingresados es:', suma/numeros)
        break
    #suma = suma + numero
    #numeros = numeros + 1
    suma += numero
    numeros += 1

