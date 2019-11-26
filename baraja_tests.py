import unittest
from unittest.mock import patch
import baraja

def mi_eligecarta(i, longitud):
    if i == longitud-1:
        return 0
    else:
        return i+1


class BarajaFuncionalTest(unittest.TestCase):

    def test_crear_baraja(self):
        b = baraja.baraja()
        self.assertEqual(len(b), 40)
        self.assertEqual(b, ['Ao', '2o', '3o', '4o', '5o', '6o', '7o', 'So', 'Co', 'Ro', 'Ac', '2c', '3c', '4c', '5c', '6c', '7c', 'Sc', 'Cc', 'Rc', 'Ae', '2e', '3e', '4e', '5e', '6e', '7e', 'Se', 'Ce', 'Re', 'Ab', '2b', '3b', '4b', '5b', '6b', '7b', 'Sb', 'Cb', 'Rb'])

        self.assertEqual(b[0], 'Ao')
        self.assertEqual(b[39], 'Rb')
        self.assertEqual(b[10], 'Ac')
        self.assertEqual(b[20], 'Ae')

    @patch('baraja.elige_carta', mi_eligecarta)
    def test_mezclar_lista(self):
        b = ['A', 'B', 'C', 'D', 'E']
        mezclada = ['A', 'C', 'D', 'E', 'B']
        b = baraja.mezclar(b)
        self.assertEqual(b, mezclada)

def class_eligecarta(self, i):
    return mi_eligecarta(i, len(self.naipes))

class BarajaObjetoTest(unittest.TestCase):
    def test_crear_baraja(self):
        b = baraja.Baraja()
        self.assertEqual(len(b.naipes), 40)
        self.assertEqual(b.naipes, ['Ao', '2o', '3o', '4o', '5o', '6o', '7o', 'So', 'Co', 'Ro', 'Ac', '2c', '3c', '4c', '5c', '6c', '7c', 'Sc', 'Cc', 'Rc', 'Ae', '2e', '3e', '4e', '5e', '6e', '7e', 'Se', 'Ce', 'Re', 'Ab', '2b', '3b', '4b', '5b', '6b', '7b', 'Sb', 'Cb', 'Rb'])

        self.assertEqual(b.naipes[0], 'Ao')
        self.assertEqual(b.naipes[39], 'Rb')
        self.assertEqual(b.naipes[10], 'Ac')
        self.assertEqual(b.naipes[20], 'Ae')

    @patch('baraja.Baraja.elige_carta', class_eligecarta)
    def test_mezclar_lista(self):
        b = baraja.Baraja()
        b.mezclar()

        self.assertEqual(b.naipes[0], 'Ao')
        self.assertEqual(b.naipes[39], '2o')
        self.assertEqual(b.naipes[10], '2c')
        self.assertEqual(b.naipes[20], '2e')

    def test_mezclar_sin_comprobar_orden(self):
        b = baraja.Baraja()
        b.mezclar()

        self.assertEqual(len(b.naipes), 40)

    def test_repartir_baraja(self):
        b = baraja.Baraja()

        jugadas = b.repartir(3,2)
        self.assertEqual(len(jugadas), 2)
        self.assertEqual(len(b.naipes), 34)
        self.assertEqual(jugadas[0], ['Ao', '3o', '5o'])
        self.assertEqual(jugadas[1], ['2o', '4o', '6o'])

    def test_repartirF_baraja(self):
        b = baraja.Baraja()
        jugadas = b.repartirF(5,3)
        self.assertEqual(len(jugadas),3)
        self.assertEqual(len(b.naipes),25)
        self.assertEqual(jugadas[0], ['Ao', '4o', '7o','Ro','3c'])
        self.assertEqual(jugadas[1], ['2o', '5o', 'So','Ac','4c'])
        self.assertEqual(jugadas[2], ['3o', '6o', 'Co','2c','5c'])

if __name__ == '__main__':
    unittest.main()