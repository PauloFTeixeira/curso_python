"""
Hooks são os testes em si

setup() => Executado antes de cada metodo de teste. Util para criar instancias de objetos 

tearDown() => Executado no final de cada médulo de teste. Util para deletar dados ou fechar banco 
de dados

"""

import unittest

class ModuloTest(unittest.TestCase):

    def setUp(self):
        """Configurações do setup"""
        pass
    
    def test_primeiro():
        pass

    def test_segundo():
        pass

    def tearDown(self):
        """Configurações do tearDown"""
        pass