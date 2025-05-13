
cateto1= int(input("Ingresa valor de cateto 1: "))
cateto2= int(input("Ingresa valor de cateto 2: "))

import math
hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)
print("La hipotenusa del triangulo es: " + str(hipotenusa))