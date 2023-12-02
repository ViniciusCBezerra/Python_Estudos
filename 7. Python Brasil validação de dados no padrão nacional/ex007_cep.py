class BuscaEndereco:
    def __init__(self,cep):
        if self.cep_eh_valido(str(cep)):
            self.cep = str(cep)
        else:
            raise ValueError('CEP inválido!!')


    def __str__(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"


    def cep_eh_valido(self,cep): 
        if len(cep) == 8:
            return True
        else:
            return False


    def formata_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"
