################################################################################
# Escribir por pantalla cada carácter de una cadena introducida por teclado.
################################################################################

my_string = input('Ingresa un texto: ')

print(my_string)

for letra in my_string:
    print(letra, end=' - ')

print()
# len es para el tamaño. len = "lenght".
for index in range(len(my_string)):
    #print(my_string[index], 'en posicion', index)
    print('[', index, '] =', my_string[index])

other_string = 'prueba'

print(other_string[0])
print(other_string[3])
print(other_string[5])