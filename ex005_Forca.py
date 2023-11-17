def Jogar():
    print('=-'*20)
    print('Bem vindo ao jogo da forca!')
    print('=-'*20)


    palavra_secreta = 'maça'.upper()
    letras_acertadas = ['_' for letra in palavra_secreta]

    acertou = enforcou = False
    erros = 0


    print(letras_acertadas)
    while not enforcou and not acertou:
        chute = str(input('Qual a letra?'))
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros +=1
            print(f'{erros} erros de 6')



        enforcou = erros == 6

        print(letras_acertadas)
        #Deixa o letras_acertadas bonito
        #v=0
        #for valor in letras_acertadas:
            #v+=1
           #if v == len(letras_acertadas):
                #print(f'{valor}')
            #else:
                #print(f'{valor} ', end='')


        if '_' not in letras_acertadas:
            acertou = True

    if acertou:
        print('=-' * 20)
        print('            Você ganhou!')
        print('=-' * 20)
    elif enforcou:
        print('=-' * 20)
        print('           Você perdeu ;(')
        print('=-' * 20)

    print('Fim do jogo')

if __name__ == '__main__':
    Jogar()