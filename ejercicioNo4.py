def ejercicio4():
    numero = int(input("numeros a introducir= "))
    listNumeros = []
    for _ in range (numero):
        numero = int(input('ingresa un numero:'))
        listNumeros.append(numero)
    print('el numero mayor es {}'.format(max(listNumeros)))
    print('el numero menor es {}'.format(min(listNumeros)))
ejercicio4()