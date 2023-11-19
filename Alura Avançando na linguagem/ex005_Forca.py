import random


def Jogar():
    Mensagem_Abertura()

    palavra_secreta = carregar_palavra_secreta()

    letras_acertadas = cria_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    acertou = enforcou = False
    erros = 0

    while not enforcou and not acertou:
        chute = Chute_Jogador()
        #Marca os chutes certos
        if chute in palavra_secreta:
            Chute_certos(palavra_secreta,chute,letras_acertadas)
        else:
            erros +=1
            print(f'{erros} erros de 7')
            desenha_forca(erros)



        enforcou = erros == 7
        print(letras_acertadas)

        if '_' not in letras_acertadas:
            acertou = True

    if acertou:
        Mensagem_ganhou()
    elif enforcou:
        Mensagem_perdeu(palavra_secreta)


def Chute_Jogador():
    chute = str(input('Qual a letra?'))
    chute = chute.strip().upper()
    return chute


def Mensagem_Abertura():
    print('=-'*20)
    print('Bem vindo ao jogo da forca!')
    print('=-'*20)


def carregar_palavra_secreta():
    arquivo = open('nomes_forca.txt', 'r')

    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    palavra_secreta = palavras[random.randint(0, len(palavras))].upper()
    return palavra_secreta


def cria_letras_acertadas(palavra):
    return ['_' for letra in palavra]

def Chute_certos(palavra_secreta,chute,letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def Mensagem_ganhou():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def Mensagem_perdeu(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == '__main__':
    Jogar()