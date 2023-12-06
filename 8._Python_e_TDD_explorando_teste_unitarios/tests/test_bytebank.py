from pytest import raises,mark
from programa.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_o_valor_de_23(self):
        entrada = '13/03/2000' # given - contexto
        esperado = 23

        funcionario_teste = Funcionario('Teste',entrada,1111)
        resultado = funcionario_teste.idade() # when - acao

        assert resultado == esperado # then - desfecho


    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_apenas_Carvalho(self):
        entrada = ' Lucas Carvalho '
        esperado = 'Carvalho'

        funcionario_lucas = Funcionario(entrada,'11/11/2000',1111)
        resultado = funcionario_lucas.sobrenome()

        assert resultado == esperado


    def test_quando_decrescimo_salario_recebe_100_mil_deve_retornar_90_mil(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome,'11/11/2000',entrada_salario)
        resultado = funcionario_teste.decrescimo_salario()


        assert resultado == esperado


    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario = 1000
        esperado = 100

        funcionario_teste = Funcionario('teste', '11/11/2000', entrada_salario)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with raises(Exception):
            entrada = 1000000

            funcionario_teste = Funcionario('teste','11/11/2011',entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado


    def test_retorna_salario_de_1000_na_funcao_salario(self):
        entrada_salario = 1000
        esperado = 1000

        funcionario_teste = Funcionario('teste', '11/11/2000', entrada_salario)
        resultado = funcionario_teste.salario

        assert resultado == esperado
