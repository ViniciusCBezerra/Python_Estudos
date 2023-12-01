from collections import Counter

texto1 = '''Quando a detecção de mudanças começa, o framework percorre todos os componentes na árvore para verificar se o estado deles mudou ou não e se o novo estado afeta a visualização. Se for o caso, a parte do DOM do componente que foi afetada pela mudança é atualizada.
Essa funcionalidade pode ter um impacto significativo no desempenho da aplicação, realizando trabalhos que podem não ser necessários, já que a maioria dos componentes pode não ser afetada pelo evento e ela sempre percorre toda a árvore.
Você deve estar se perguntando: "Mas Vinny, por que você está explicando isso? Este artigo não é sobre Angular Signals?"'''

texto2 = '''O design em movimento ou motion graphics tem se mostrado uma ferramenta essencial na era digital, especialmente nas mídias sociais. Com a sua capacidade de capturar a atenção do público, transmitir informações de forma rápida e criar conexões emocionais, o design em movimento tem um papel crucial no ambiente cada vez mais competitivo das mídias sociais. Ele permite transformar postagens estáticas em experiências interativas e envolventes, usando desde animações simples até vídeos complexos.
Além do apelo visual, o motion graphics é altamente usado na comunicação. Estudos indicam que os usuários de mídias sociais se engajam mais com conteúdos visuais, e informações apresentadas visualmente são mais facilmente retidas do que as apresentadas apenas em texto. Ao utilizar animação e vídeo, o design em movimento vai além, apresentando informações de maneira ainda mais atrativa e memorável. Além disso, é uma ferramenta poderosa para evocar emoções e criar uma sensação de personalidade e estilo da marca, o que pode resultar em maior engajamento das pessoas usuárias e reconhecimento da marca.'''
print('TEXTO 1')
contador_texto2 = Counter(texto2.lower())
total_caracteres2 = sum(contador_texto2.values())
proporcoes = [(letra, frequencia / total_caracteres2) for letra,frequencia in contador_texto2.items()]
proporcoes = Counter(dict(proporcoes))
dez_mais_usadas = proporcoes.most_common(10)
for caracteres,proporcao in dez_mais_usadas:
    print(f'"{caracteres}" => {proporcao * 100:.2f}%')
print()
print('TEXTO 2')
contador_texto1 = Counter(texto1.lower())
total_caracteres1 = sum(contador_texto1.values())
proporcoes = [(letra, frequencia / total_caracteres1) for letra,frequencia in contador_texto1.items()]
proporcoes = Counter(dict(proporcoes))
dez_mais_usadas = proporcoes.most_common(10)
for caracteres,proporcao in dez_mais_usadas:
    print(f'"{caracteres}" => {proporcao * 100:.2f}%')
