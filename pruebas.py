import unittest
import adn as ADN

class pruebas(unittest.TestCase):
    def test_corresponden(self):
        self.assertEqual(ADN.corresponden('AGATA', 'TCTAT'),True)
        self.assertEqual(ADN.corresponden('AGATA', 'GACCG'),False)
        self.assertEqual(ADN.corresponden('TACA', 'ATGT'), True)
        self.assertEqual(ADN.corresponden('ATACA', 'GCC'), False)
        self.assertRaises(TypeError,ADN.corresponden, 'AGATA', 'FIN')
    def test_es_cadena_valida(self):
        self.assertEqual(ADN.es_cadena_valida('AGATA'), True)
        self.assertEqual(ADN.es_cadena_valida('AGATS'), False)
        self.assertEqual(ADN.es_cadena_valida('CANTAR'), False)
        self.assertEqual(ADN.es_cadena_valida('TAGA'), True)
        self.assertRaises(TypeError,ADN.es_cadena_valida, '1234')
    def test_es_base(self):
        self.assertEqual(ADN.es_base(A), True)
        self.assertEqual(ADN.es_base(B), False)
        self.assertEqual(ADN.es_base(C), True)
        self.assertEqual(ADN.es_base(D), False)
        self.assertRaises(TypeError,ADN.es_base, 'CASA')
    def test_es_subcadena(self):
        self.assertEqual(ADN.es_subcadena(TAGA, TAG), True)
        self.assertEqual(ADN.es_subcadena(GATA, ATCT), False)
        self.assertEqual(ADN.es_subcadena(TAGA, CCTG), False)
        self.assertEqual(ADN.es_subcadena(ATCT, AT), True)
        self.assertRaises(TypeError,ADN.es_subcadena, 'SOFA', 'CRYSTAL')

if __name__== 'main':
    unittest.main()
