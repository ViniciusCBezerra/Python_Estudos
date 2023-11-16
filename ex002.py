class Bola:
    def __init__(self, cor, circunferencia,material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self,nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        print(f'A cor da Bola é {self.cor}')


bola = Bola('Azul', '10cm' , 'Pano')
bola.mostraCor()
bola.trocaCor('Preto')
bola.mostraCor()