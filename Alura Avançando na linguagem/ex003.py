class Quadrado:
    def __init__(self , lado):
        self.lado = lado
        self.primeirolado = lado

    def mudaLado(self,novo_lado):
        self.lado = novo_lado

    def voltarLado(self):
        self.lado = self.primeirolado

    def Area(self):
        self.area = self.lado*self.lado
        print(f'A área do quadrado é de {self.area}')


quadrado=Quadrado(6)
print(quadrado.lado)
quadrado.mudaLado(9)
print(quadrado.lado)
quadrado.Area()

