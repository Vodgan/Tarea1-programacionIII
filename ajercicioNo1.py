def ejercicio1():
    limite = 100
    indice=1
    indice2=0
#comentario de prueba para cambio con git
    while indice <=limite:
        if indice % 2:
            print('Es impar - inidice = ' + str(indice))
            indice2+=1
        indice+=1

    print('Total de numeros impares =' + str(indice2))
ejercicio1()