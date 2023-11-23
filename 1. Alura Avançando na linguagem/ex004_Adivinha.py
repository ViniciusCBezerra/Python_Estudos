import random

def Jogar():
    print('=-'*20)
    print('JOGO DA SORTE')
    print('=-'*20)
    maximo_tentativas = 3
    erros = numero_tentativa = numero_tentativas = numero_secreto = nivel = 0
    pontos = 100

    while nivel != 1 and nivel != 2 and nivel != 3:
        nivel= int(input('Qual nível de dificuldade deseja? (1 - fácil , 2 - médio , 3 - dificil): '))


    if nivel == 1:
        numero_secreto = random.randint(1, 10)
        while numero_tentativas < maximo_tentativas:
            print(f'Tentativa {numero_tentativas+1} de {maximo_tentativas}')
            numero_tentativa = int(input('Digite um número entre 1 e 10 e tente sua sorte: '))

            if numero_tentativa != numero_secreto:
                erros+=1

            if numero_tentativa < 1 or numero_tentativa > 10:
                print('Erro, você digitou um número inválido')
                continue

            print(f'Você digitou {numero_tentativa}!')

            if numero_tentativa > numero_secreto:
                numero_tentativas += 1
                print('Você errou,Digite um número menor!')
            elif numero_tentativa < numero_secreto:
                numero_tentativas += 1
                print('Você errou, Digite um número maior!')
            elif numero_tentativa == numero_secreto:
                break


    elif nivel == 2:
        numero_secreto = random.randint(1, 100)
        while numero_tentativas < maximo_tentativas:
            print(f'Tentativa {numero_tentativas+1} de {maximo_tentativas}')
            numero_tentativa = int(input('Digite um número entre 1 e 100 e tente sua sorte: '))

            if numero_tentativa != numero_secreto:
                erros += 1

            if numero_tentativa < 1 or numero_tentativa > 100:
                print('Erro, você digitou um número inválido')
                continue


            print(f'Você digitou {numero_tentativa}!')


            if numero_tentativa > numero_secreto:
                numero_tentativas += 1
                print('Você errou,Digite um número menor!')
            elif numero_tentativa < numero_secreto:
                numero_tentativas += 1
                print('Você errou, Digite um número maior!')
            elif numero_tentativa == numero_secreto:
                break


    elif nivel == 3:
        numero_secreto = random.randint(1, 1000)
        while numero_tentativas < maximo_tentativas:
            print(f'Tentativa {numero_tentativas+1} de {maximo_tentativas}')
            numero_tentativa = int(input('Digite um número entre 1 e 1000 e tente sua sorte: '))

            if numero_tentativa != numero_secreto:
                erros += 1

            if numero_tentativa < 1 or numero_tentativa > 1000:
                print('Erro, você digitou um número inválido')
                continue

            print(f'Você digitou {numero_tentativa}!')


            if numero_tentativa > numero_secreto:
                numero_tentativas += 1
                print('Você errou,Digite um número menor!')
            elif numero_tentativa < numero_secreto:
                numero_tentativas += 1
                print('Você errou, Digite um número maior!')
            elif numero_tentativa == numero_secreto:
                break

    if numero_tentativa == numero_secreto:
        pontos += 500
    else:
        pontos -= 5*erros


    if numero_tentativa == numero_secreto:
        print('=-' * 20)
        print(f'Você ganhou com {numero_tentativas} tentativas!')
        print('=-' * 20)
        print()
    else:
        print('=-' * 20)
        print(f'Você perdeu! Mais sorte da proxima vez!')
        print('=-' * 20)
        print()
    print('=-'*20)
    print(f'Você fez um total de {pontos} pontos!')
    print('=-'*20)
    print()
    print('=-'*20)
    print('Fim do jogo')
    print('=-'*20)

if __name__ == '__main__':
    Jogar()