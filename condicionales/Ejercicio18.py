################################################################################
#Realiza un programa que pida el dí­a de la semana (del 1 al 7) y escriba 
#el dí­a correspondiente. 
#Si introducimos otro número nos da un error.
################################################################################

dia = int(input('Introduce un numero de dia: '))

match dia:
    case 1:
        print('El dia es lunes.')
    case 2:
        print('El dia es martes.')
    case 3:
        print('El dia es miercoles.')
    case 4:
        print('El dia es jueves.')
    case 5:
        print('El dia es viernes.')
    case 6:
        print('El dia es sabado.')
    case 7:
        print('El dia es domingo.')
    case _:
        print('El dia elegido no existe.')
