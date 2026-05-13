print('Sistema de Cajero Automatico')
salir = False
saldo = 1000

while not salir:
    print('''Operaciones que puedes realizar:
        1. Consultar saldo
        2. Retirar
        3. Depositae
        4. Salir''')
    opcion = int(input('Selecciona una opción: '))

    if opcion == 1:
        print(f'Tu saldo es: ${saldo:.2f}\n')

    elif opcion == 2:
        monto = float(input('Ingresa el Monto a retirar: '))
        if monto > saldo:
            print('No tienes saldo suficiente\n')
        else:
            saldo -= monto
            print(f'Tu saldo actual es: ${saldo:.2f}')

    elif opcion == 3:
        monto = float(input('Ingresa el Monto a depositar: '))
        saldo += monto
        print(f'Tu saldo actual es: ${saldo:.2f}\n')

    elif opcion == 4:
        salir = True
        print('Hasta Luego...')

    else:
        print('Opcion no valida...\n')




