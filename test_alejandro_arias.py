import unittest
from Examen2 import MiClase

class TestMiClase(unittest.TestCase):
    def setUp(self):
        self.album = MiClase(5, 100, 15, ["cancion 1", "cancion 2", "cancion 3"], [0.5, 0.6, 0.4])
        
    def test_ObtieneValencia_cuenta_impares(self):
        resultado = self.album.ObtieneValencia(7591360)  
        self.assertEqual(resultado, 5)  

    def test_ObtieneValencia_no_es_cero_con_impares(self):
        resultado = self.album.ObtieneValencia(5)
        self.assertNotEqual(resultado, 0)  

    def test_DivisibleTempo_no_es_None(self):
        resultado = self.album.DivisibleTempo(10)
        self.assertIsNotNone(resultado)  

    def test_DivisibleTempo_resultado_no_es_None(self):
        resultado = self.album.DivisibleTempo(10)
        self.assertIsNot(resultado, None) 

    def test_ObtieneMasBailable_lista_vacia_da_None(self):
        resultado = self.album.ObtieneMasBailable([])
        self.assertIsNone(resultado)  

    def test_ObtieneMasBailable_devuelve_mayor_valor(self):
        resultado = self.album.ObtieneMasBailable([0.5, 0.6, 0.4])
        self.assertTrue(resultado == 0.6) 

    def test_VerificaListaCanciones_todo_valido_es_true(self):
        resultado = self.album.VerificaListaCanciones(["c1", "c2"])
        self.assertIs(resultado, False) 

    def test_VerificaListaCanciones_con_None_es_false(self):
        resultado = self.album.VerificaListaCanciones(["c1", None])
        self.assertFalse(resultado)  

if __name__ == "__main__":
    unittest.main()
