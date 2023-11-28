from random import randint


class Programa:
    def __init__(self,lista_do_programa):
        valor = randint(1,100)
        lista_do_programa.append(valor)



minha_lista_aleatoria = list()
for vezes in range(0,10):
    Programa(minha_lista_aleatoria)
print(minha_lista_aleatoria)