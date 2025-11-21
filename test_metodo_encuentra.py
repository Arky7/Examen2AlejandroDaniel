import unittest
from Examen2 import MiClase

class TestMiClase(unittest.TestCase):
    def setUp(self):
        self.album = MiClase(5, 100, 15, ["cancion 1", "cancion 2", "cancion 3"], [0.5, 0.6, 0.4])

    def test_Encuentra_error_si_no_entero(self):
        with self.assertRaises(ValueError):
            self.album.Encuentra([1, "a", 3], 3)

if __name__ == "__main__":
    unittest.main()
