import os
from datetime import timedelta

#este modulo es para funciones adicionales del triatlon

def hacerfecha(): #esta funcion nos devolvera la fecha bien realizada dependiendo del mes y los dias del mes y que no sobrepase el año en el que estamos sea coherente
    hecho = False
    while not hecho:
        verif = False
        while not verif:
            print('--RELLENE LOS SIGUIENTES APARTADOS PARA CREAR LA FECHA--')
            dia = input('Escriba el día -> ')
            mes = input('Escriba el mes -> ')
            año = input('Escriba el año -> ')
            if dia.isdigit() and mes.isdigit() and año.isdigit():
                dia = int(dia)
                mes = int(mes)
                año = int(año)
                verif = True
            else:
                input('Los datos no son correctos, tienen que ser numéricos. Presione Enter para continuar.')

        if 1925 < año <= 2025:
            dias_validos = 31
            if mes in [4, 6, 9, 11]:
                dias_validos = 30
            elif mes == 2:
                bis = input('¿El año es bisiesto? (1->Sí | 2->No): ')
                if bis == '1':
                    dias_validos = 29
                else:
                    dias_validos = 28

            if 1 <= dia <= dias_validos and 1 <= mes <= 12:
                fecha = f"{dia:02d}/{mes:02d}/{año}"
                verificar = True
                while verificar:
                    acep = input(f'¿Está satisfecho con la fecha? - {fecha} - \n(1->Sí | 2->No): ')
                    if acep == '1':
                        return fecha
                    elif acep == '2':
                        input('Volverá a introducir los datos. Presione Enter para continuar.')
                        verificar = False
                        verif = False
                    else:
                        input('Opción no válida. Presione Enter para continuar.')
            else:
                input('Día o mes fuera de rango. Presione Enter para continuar.')
        else:
            input('Año no válido. Debe estar entre 1926 y 2024. Presione Enter para continuar.')

            
def hacerdni(): #esta funcion nos devolvera una variable con los 8 numeros del DNI
    verif= False
    while not verif:
        print('-Recordatorio, el DNI contiene 8 números-')
        nums= input('Introduce el DNI del Participante ->')
        letra= input('Escriba la letra del DNI ->')
        if nums.isdigit() and len(nums)==8 and len(letra)==1 and str(letra):
            dni=nums+letra
            verif= True
            return dni
        else:
            input('No es un DNI valido, vuelva a intertarlo')
            os.system('cls')

def resultado_pruebas(): #esta funcion en la cual he usado el modulo datetime nos devolvera el tiempo de los resultados 
    hecho= False
    while not hecho:
        verif= False
        while not verif: #en estos primros apartados conseguiremos las variables de hora,minutos y segundos para despues implementarlas en la funcion timedelta intentado tener la sintaxsis del resultado 00:00:00
            hora= input('Escriba cuantas horas tardó -> ')
            if len(hora) != 2:
                hora = '0'+ hora
            if hora.isdigit():
                verif= True
                hora= int(hora)
            else:
                print('Por favor introduce una unidad válida')
        verif= False
        while not verif:
            minutos= input('Escriba cuantos minutos tardó -> ')
            if len(minutos) != 2:
                minutos = '0'+ minutos
            if minutos.isdigit():
                verif= True
                minutos= int(minutos)
            else:
                print('Por favor introduce una unidad válida')
        verif= False
        while not verif:
            segundos= input('Escriba cuantos minutos tardó -> ')
            if len(segundos) != 2:
                segundos = '0'+ segundos
            if segundos.isdigit():
                verif= True
                segundos= int(segundos)
            else:
                print('Por favor introduce una unidad válida')
        tiempo= timedelta(hours=hora,minutes=minutos,seconds=segundos) #desde las variables se las pasamos a la funcion 
        verif= False
        while not verif:
            opc= input(f'¿Este es el tiempo correcto del participante? - {tiempo} -\n SI -> 1|NO -> 2 \n ->') #por ultimo verificamos que asi es el resultado de la prueba 
            if opc == '1':
                verif= True
                hecho= True
                return tiempo
            elif opc== '2':
                input('Volverá a escribir el tiempo')
                verif= True
            else:
                input('No es una opción válida')