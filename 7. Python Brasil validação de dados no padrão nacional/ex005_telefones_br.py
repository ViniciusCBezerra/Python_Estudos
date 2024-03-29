import re

class TelefoneBr:
    def __init__(self,telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError('Número incorreto')


    def __str__(self):
        return self.formatar_numero()


    def valida_telefone(self,telefone):
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao,telefone)
        if resposta:
            return True
        else:
            return False


    def formatar_numero(self):
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao,self.numero)
        numero_formatado_com_pais = (
            f'+{resposta.group(1)}'
            f'({resposta.group(2)})'
            f'{resposta.group(3)}'
            f'-{resposta.group(4)}'
        )
        numero_formatado_sem_pais = (
            f'({resposta.group(2)})'
            f'{resposta.group(3)}'
            f'-{resposta.group(4)}'
        )

        if resposta.group(1) == None:
            return numero_formatado_sem_pais
        else:
            return numero_formatado_com_pais