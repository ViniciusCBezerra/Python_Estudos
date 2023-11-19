class Conta:
    def __init__(self , numero,titular,saldo,limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'O seu extrato {self.__titular} é de R${self.__saldo:.2f}')

    def depositar(self,valor):
        self.__saldo +=valor
        print(f'Você {self.__titular} depositou R${valor:.2f} na sua conta')

    def __pode_sacar(self,valor_a_sacar):
        maximo_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= maximo_sacar

    def sacar(self,valor):
        if self.pode_sacar(valor):
            self.__saldo -= valor
            print(f'Você {self.__titular} sacou R${valor:.2f} na sua conta')
        else:
            print(f'Você não possui o limite para sacar o valor de R${valor}')
            print(f'O valor maximo é de R${self.__saldo + self.__limite}')

    def transferir(self,valor,destino):
        self.sacar(valor)
        destino.depositar(valor)
        print(f'Você {self.__titular} transferiu R${valor:.2f} para {destino._Conta__titular}')

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self,novo_saldo):
        self.__saldo = novo_saldo

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self,novo_titular):
        self.__titular = novo_titular

    @property
    def limite(self):
        self.__limite

    @limite.setter
    def limite(self,novo_limite):
        self.__limite = novo_limite

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}

codigo = Conta.codigos_bancos()
print(codigo["BB"])