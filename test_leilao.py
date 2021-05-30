from unittest import TestCase
from python_9_testes_automatizados_tdd.dominio import Usuario, Lance, Leilao
from python_9_testes_automatizados_tdd.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):
        self.vini = Usuario('Vini', 500.0)
        self.lance_vini = Lance(self.vini, 100.0)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        panai = Usuario('Panai', 500.0)
        lance_panai = Lance(panai, 150.0)

        self.leilao.propoe(self.lance_vini)
        self.leilao.propoe(lance_panai)

        menor_valor_esperado = 100
        maior_valor_esperado = 150

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)


    def test_deve_permitir_propor_um_valor_em_ordem_decrescente(self):

        with self.assertRaises(LanceInvalido):
            panai = Usuario('Panai', 500.0)
            lance_panai = Lance(panai, 150.0)

            self.leilao.propoe(lance_panai)
            self.leilao.propoe(self.lance_vini)

    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_leilao_tiver_apenas_um_lance(self):
        self.leilao.propoe(self.lance_vini)

        self.assertEqual(100.0, self.leilao.menor_lance)
        self.assertEqual(100.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_o_leilao_tiver_tres_lances(self):

        panai = Usuario('Panai', 500.0)
        gordiz = Usuario('Gordiz', 500.0)

        lance_panai = Lance(panai, 150.0)
        lance_gordiz = Lance(gordiz, 200.0)

        self.leilao.propoe(self.lance_vini)
        self.leilao.propoe(lance_panai)
        self.leilao.propoe(lance_gordiz)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_vini)

        quantidade_de_lances_recebidos = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebidos)


    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        panai = Usuario('Panai', 500.0)
        lance_da_panai = Lance(panai, 200.0)

        self.leilao.propoe(self.lance_vini)
        self.leilao.propoe(lance_da_panai)

        quantidade_de_lances_recebido = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebido)

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_vini200 = Lance(self.vini, 200.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_vini)
            self.leilao.propoe(lance_do_vini200)