# coding: utf-8

from source.gera_senha_kleyton import GeraSenha
import unittest

class TestGeraSenha(unittest.TestCase):
    def test_gera_senha(self):
        """
        Como é uma funcão que tem retorno aleatório os casos de teste são repetidos várias vezes para garantir
        a eficácia do teste, falha na primeira vez é uma chance pequena.
        """
        print("São 200k de testes, por favor aguarde...")
        [self.assertNotEqual(GeraSenha().gera_senha(), GeraSenha().gera_senha()) for x in range(100000)]  # Senha imediatamente repetida
        [self.assertNotEqual(len(GeraSenha().gera_senha()), 0) for x in range(100000)]  # Senha vazia


if __name__ == '__main__':
    unittest.main()

