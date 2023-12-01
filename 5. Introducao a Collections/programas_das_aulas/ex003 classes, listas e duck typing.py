from abc import ABCMeta,abstractmethod
from functools import total_ordering

class Conta(metaclass=ABCMeta):
    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self,valor):
        self._saldo += valor

    @abstractmethod
    def passa_mes(self,):
        pass
    def __str__(self):
        return f"Código: {self._codigo} <<  Saldo: {self._saldo} <<"

class ContaCorrente(Conta):
    def passa_mes(self):
        self._saldo -= 2

class ContaPoupança(Conta):
    def passa_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    def passa_mes(self):
        self._saldo *= 1.09

@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self,valor):
        self._saldo += valor

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        else:
            return self._codigo == other._codigo and self._saldo == other._saldo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        else:
            return self._codigo < other._codigo

    def __str__(self):
        return f'>> Código: {self._codigo}  Saldo: {self._saldo} <<'


conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_mes()

conta17 = ContaPoupança(17)
conta17.deposita(1000)
conta17.passa_mes()

conta18 = ContaInvestimento(18)
conta18.deposita(1500)

contas = [conta16,conta17,conta18]
for conta in contas:
    conta.passa_mes() #duck typing
#Parte 2

conta_gui = ContaSalario(17)
conta_gui.deposita(500)

conta_dani = ContaSalario(3)
conta_dani.deposita(1000)

conta_paulo = ContaSalario(133)
conta_paulo.deposita(500)

contas = [conta_gui,conta_dani,conta_paulo]

for conta in sorted(contas):
    print(conta)

print(conta_gui <= conta_gui)