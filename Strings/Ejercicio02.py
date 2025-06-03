# my_string='Este es un texto.'
# my_string.capitalize()

# print(my_string.capitalize())
# print(my_string.lower())
# print(my_string.title())
# print(my_string.startswith('Este'))
# print(my_string.startswith('Esta'))

my_str_1 = input('Ingresa una cadena de texto: ')
my_str_2 = input('Ingresa las primeras letras de la cadena anterior: ')

if my_str_1.startswith(my_str_2):
    print('"', my_str_1, '"', ' si comienza con ', '"', my_str_2, '"')
else:
    print('"', my_str_1, '"', ' no comienza con ', '"', my_str_2, '"')
    
