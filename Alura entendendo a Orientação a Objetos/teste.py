def cria_conta(numero,titular,saldo,limite):
    conta = {"numero": numero , "titular": titular , "saldo": saldo , "limite": limite}
    return conta


def depositar(conta,valor):
    conta["saldo"] += valor
    print(f'Você depositou R${valor}')


def sacar(conta,valor):
    conta["saldo"] -= valor
    print(f'Você sacou R${valor}')


def extrato(conta):
    print(f'O extrato da conta é R${conta["saldo"]}')