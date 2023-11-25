import re
endereco = 'Rua das flores 72,  apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120'

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao.search(endereco) #match or none

if busca:
    cep = busca.group() #retorna o cep do endereço

    print(cep)
