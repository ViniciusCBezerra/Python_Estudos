from Alura import ex004_Adivinha, ex005_Forca


def Jogos():
    print('=-'*20)
    print('Escolha um jogo!')
    print('=-'*20)

    jogo = int(input('Jogo da adivinhação - 1 / Jogo da forca - 2 :'))

    if jogo == 1:
        ex004_Adivinha.Jogar()
    elif jogo == 2:
        ex005_Forca.Jogar()

if __name__ == '__main__':
    Jogos()
