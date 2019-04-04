import unittest
import adn as cadena

class pruebas(unittest.TestCase):
    def test_corresponden(self):
        self.assertEqual(cadena.corresponden('AGATA', 'TCTAT'),True)
        self.assertEqual(cadena.corresponden('AGATA', 'GACCG'),False)
        self.assertEqual(cadena.corresponden('TACA', 'ATGT'), True)
        self.assertEqual(cadena.corresponden('ATACA', 'GCC'), False)
        self.assertRaises(TypeError,cadena.corresponden, 'AGATA', 'FIN')
    def test_es_cadena_valida(self):
        self.assertEqual(cadena.es_cadena_valida('AGATA'), True)
        self.assertEqual(cadena.es_cadena_valida('AGATS'), False)
        self.assertEqual(cadena.es_cadena_valida('CANTAR'), False)
        self.assertEqual(cadena.es_cadena_valida('TAGA'), True)
        self.assertRaises(TypeError,cadena.es_cadena_valida, 1234)
    def test_es_base(self):
        self.assertEqual(cadena.es_base('A'), True)
        self.assertEqual(cadena.es_base('B'), False)
        self.assertEqual(cadena.es_base('C'), True)
        self.assertEqual(cadena.es_base('D'), False)
        self.assertRaises(TypeError,cadena.es_base, 1)
    def test_es_subcadena(self):
        self.assertEqual(cadena.es_subcadena('TAGA', 'TAG'), True)
        self.assertEqual(cadena.es_subcadena('GATA', 'ATCT'), False)
        self.assertEqual(cadena.es_subcadena('TAGA', 'CCTG'), False)
        self.assertEqual(cadena.es_subcadena('ATCT', 'AT'), True)
        self.assertRaises(TypeError,cadena.es_subcadena, 'SOFA', 'CRYSTAL')
    def test_obtener_complemento(self):
        self.assertEqual(cadena.obtener_complemento('A'),'T')
        self.assertEqual(cadena.generar_cadena_complementaria('AGATA'),'TCTAT')
        self.assertEqual(cadena.calcular_correspondencia('AGATA','TCTAT'),100)
        self.assertEqual(cadena.reparar_dano('APATA','G'),'AGATA')
    def test_obtener_secciones(self):
        self.assertEqual(cadena.obtener_secciones('agtgtc',3),['ag', 'tg', 'tc'])
        self.assertRaises(TypeError,cadena.obtener_secciones,'asdsdfdsf',0)
    def test_obtener_complementos(self):
        self.assertEqual(cadena.obtener_complementos(['gtgt','gtca','caca','taga']),['CACA', 'CAGT', 'GTGT', 'ATCT'])
        self.assertRaises(TypeError,cadena.obtener_complementos,1,1)
    def test_unir_cadenas(self):
        self.assertEqual(cadena.unir_cadena(['agt','cta','gcc']),'agtctagcc')
        self.assertEqual(cadena.unir_cadena(['agc','ggg','ttt']),'agcgggttt')
        self.assertRaises(TypeError, cadena.unir_cadena,['agt','gcc','ugt'])
    def test_complementar_cadenas(self):
        self.assertEqual(cadena.complementar_cadenas(['agt','cta','gcc']),'TCAGATCGG')
        self.assertEqual(cadena.complementar_cadenas(['agc','ggg','ttt']),'TCGCCCAAA')


if __name__== 'main':
    unittest.main()
