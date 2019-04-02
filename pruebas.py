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
        self.assertRaises(TypeError,ADN.es_cadena_valida, 1234)
    def test_es_base(self):
        self.assertEqual(ADN.es_base('A'), True)
        self.assertEqual(ADN.es_base('B'), False)
        self.assertEqual(ADN.es_base('C'), True)
        self.assertEqual(ADN.es_base('D'), False)
        self.assertRaises(TypeError,ADN.es_base, 1)
    def test_es_subcadena(self):
        self.assertEqual(ADN.es_subcadena('TAGA', 'TAG'), True)
        self.assertEqual(ADN.es_subcadena('GATA', 'ATCT'), False)
        self.assertEqual(ADN.es_subcadena('TAGA', 'CCTG'), False)
        self.assertEqual(ADN.es_subcadena('ATCT', 'AT'), True)
        self.assertRaises(TypeError,ADN.es_subcadena, 'SOFA', 'CRYSTAL')
    def test_obtener_complemento(self):
        self.assertEqual(ADN.obtener_complemento('A'),'T')
        self.assertEqual(ADN.generar_cadena_complementaria('AGATA'),'TCTAT')
        self.assertEqual(ADN.calcular_correspondencia('AGATA','TCTAT'),100)
        self.assertEqual(ADN.reparar_dano('APATA','G'),'AGATA')
    def test_obtener_secciones(self):
        self.assertEqual(ADN.obtener_secciones('agtgtc',3),['ag', 'tg', 'tc'])
        self.assertRaises(TypeError,ADN.obtener_secciones,'asdsdfdsf',0)
    def test_obtener_complementos(self):
        self.assertEqual(ADN.obtener_complementos(['gtgt','gtca','caca','taga']),['CACA', 'CAGT', 'GTGT', 'ATCT'])
    def test_unir_cadenas(self):
        self.assertEqual(ADN.unir_cadenas(['agt','cta','gcc']),'agtctagcc')
        self.assertEqual(ADN.unir_cadenas(['agc','ggg','ttt']),'agcgggttt')
        self.assertRaises(TypeError, ADN.unir_cadenas,['agt','gcc','ugt'])
    def test_complementar_cadenas(self):
        self.assertEqual(ADN.complementar_cadenas(['agt','cta','gcc']),'tcagatcgg')
        self.assertEqual(ADN.complementar_cadenas(['agc','ggg','ttt']),'tcgcccaaa')

if __name__== 'main':
    unittest.main()
