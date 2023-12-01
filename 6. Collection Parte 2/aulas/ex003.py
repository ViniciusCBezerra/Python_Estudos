from collections import defaultdict
from collections import Counter
class Conta:
    def __init__(self):
        print('Criando uma conta!')

meu_texto = "Bem vindo meu nome é vinicius eu gosto do meu nome e gosto de ir à igreja todo domingo e sabado quero ser musico tocando flauta transversal"
# meu_texto = meu_texto.lower()
# aparicoes = defaultdict(int)
# for palavra in meu_texto.split():
#     aparicoes[palavra] += 1
# print(aparicoes)

aparicoes = Counter(meu_texto.split())
print(aparicoes)

