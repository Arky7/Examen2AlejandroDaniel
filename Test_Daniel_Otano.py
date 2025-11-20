import unittest
from Examen2 import MiClase

class TestMiClase(unittest.TestCase):

    def setUp(self):
        self.obj = MiClase(5, 120, 12, ["A", "B"], [0.1, 0.5])

    def test_ObtieneValencia_contar_impares(self):
        resultado = self.obj.ObtieneValencia(1234567)
        self.assertEqual(resultado, 4)  # 1,3,5,7

    def test_ObtieneValencia_sin_impares(self):
        resultado = self.obj.ObtieneValencia(2468)
        self.assertEqual(resultado, 0)

    def test_DivisibleTempo_divisores_correctos(self):
        self.assertEqual(self.obj.DivisibleTempo(10), [1, 2, 5, 10])

    def test_DivisibleTempo_numero_primo(self):
        self.assertEqual(self.obj.DivisibleTempo(7), [1, 7])

    def test_ObtieneMasBailable_lista_normal(self):
        valor = self.obj.ObtieneMasBailable([0.2, 0.8, 0.1])
        self.assertEqual(valor, 0.8)

    def test_ObtieneMasBailable_lista_vacia(self):
        self.assertIsNone(self.obj.ObtieneMasBailable([]))

    def test_VerificaListaCanciones_sin_None(self):
        self.assertTrue(self.obj.VerificaListaCanciones(["A", "B", "C"]))

    def test_VerificaListaCanciones_con_None(self):
        self.assertFalse(self.obj.VerificaListaCanciones(["A", None, "C"]))

    def test_ObtieneValencia_error_si_no_es_numero(self):
        with self.assertRaises(ValueError):
            self.obj.ObtieneValencia("ABC")   

    def test_DivisibleTempo_numero_negativo_lista_vacia(self):
        resultado = self.obj.DivisibleTempo(-5)
        self.assertEqual(resultado, [])  
    

if __name__ == "__main__":
    unittest.main()
