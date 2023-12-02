from ex002_classes import Documento
from validate_docbr import CNPJ

exemplo_cpf = '44691811885'
cpf = Documento.CriaDocumento(exemplo_cpf)
exemplo_cnpj = '03792269000146'
cnpj = Documento.CriaDocumento(exemplo_cnpj)

print(f'Formatado: {cpf}')
print(f'Formatado: {cnpj}')
