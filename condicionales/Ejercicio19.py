################################################################################
#Escribe un programa que pida un número entero entre uno y doce e imprima el 
#número de días que tiene el mes correspondiente.
#Si introducimos otro número nos da un error.
################################################################################

month = int(input('Ingresa el numero del mes: '))

match month:
    case 1: 
        print('Enero. Tiene 31 dias.')
    case 2: 
        print('febrero. Tiene 28 dias.')
    case 3: 
        print('Marzo. Tiene 31 dias.')
    case 4: 
        print('Abril. Tiene 30 dias.')
    case 5: 
        print('Mayo. Tiene 31 dias.')
    case 6: 
        print('Junio. Tiene 30 dias.')
    case 7: 
        print('Julio. Tiene 31 dias.')
    case 8: 
        print('Agosto. Tiene 31 dias.')
    case 9: 
        print('Septiembre. Tiene 30 dias.')
    case 1: 
        print('Octubre. Tiene 31 dias.')
    case 11:
        print('Noviembre. Tiene 30 dias.')
    case 12:
        print('Diciembre. Tiene 31 dias.')