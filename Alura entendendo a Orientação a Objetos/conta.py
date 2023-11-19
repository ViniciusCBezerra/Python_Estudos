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

    def sacar(self,valor):
        self.__saldo -=valor
        print(f'Você {self.__titular} sacou R${valor:.2f} na sua conta')

    def transferir(self,valor,destino):
        self.sacar(valor)
        destino.depositar(valor)
        print(f'Você {self.__titular} transferiu R${valor:.2f} para {destino._Conta__titular}')

conta = Conta(123,'Vinicius',55.0,1000.0)
conta2 = Conta(129,'Marcos',150.0,3000.0)
conta.depositar(100.0)
conta.extrato()
conta.sacar(75.0)
conta.extrato()

conta2.transferir(50.0,conta)