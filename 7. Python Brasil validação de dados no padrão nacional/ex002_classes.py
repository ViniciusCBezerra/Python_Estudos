from validate_docbr import CPF,CNPJ


class Documento:
    @staticmethod
    def CriaDocumento(documento):
        if len(documento) == 11:
            return DocCPF(documento)
        elif len(documento) == 14:
            return DocCNPJ(documento)
        else:
            raise ValueError('Quantidade de digitos incorreta!')


class DocCPF:
    def __init__(self,cpf):
        if self.valida(cpf):
            self.cpf = cpf
        else:
            raise ValueError('CPF inválido!!')

    def __str__(self):
        return self.format()

    def valida(self,cpf):
        validador = CPF()
        return validador.validate(cpf)


    def format(self):
        return CPF().mask(self.cpf)


class DocCNPJ:
    def __init__(self,cnpj):
        if self.valida(cnpj):
            self.cnpj = cnpj
        else:
            raise ValueError('CNPJ inválido!!')

    def __str__(self):
        return self.format()

    def valida(self,cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)


    def format(self):
        return CNPJ().mask(self.cnpj)

