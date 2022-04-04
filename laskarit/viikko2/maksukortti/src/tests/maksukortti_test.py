import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        kortti = Maksukortti(10)

        kortti.syo_edullisesti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 7.5 euroa")
    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        kortti = Maksukortti(10)

        kortti.syo_maukkaasti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 6 euroa")

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(10)

        kortti.syo_maukkaasti()
        kortti.syo_maukkaasti()
        # nyt kortin saldo on 2
        kortti.syo_edullisesti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 2 euroa")

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(10)

        kortti.syo_maukkaasti()
        kortti.syo_maukkaasti()
	# nyt kortin saldo on 2
        kortti.syo_maukkaasti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 2 euroa")

    def test_negatiivinen_summa_ei_muuta_saldoa(self):
        kortti = Maksukortti(10)
        kortti.lataa_rahaa(-20)

        self.assertEqual(str(kortti), "Kortilla on rahaa 10 euroa")

    def test_syo_edullisesti_nollaa_saldon(self):
        kortti = Maksukortti(10)

        kortti.syo_edullisesti()
        kortti.syo_edullisesti()
        kortti.syo_edullisesti()
	# nyt kortin saldo on 2.5
        kortti.syo_edullisesti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 0.0 euroa")

    def test_syo_maukkaasti_nollaa_saldon(self):
        kortti = Maksukortti(12)

        kortti.syo_maukkaasti()
        kortti.syo_maukkaasti()
        # nyt kortin saldo on 4
        kortti.syo_maukkaasti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 0 euroa")
