import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varastoon_lisaa_liikaa_tavaraa(self):
        varastossa_tilaa = self.varasto.paljonko_mahtuu()

        self.varasto.lisaa_varastoon(varastossa_tilaa)
        self.varasto.lisaa_varastoon(1)
        self.assertAlmostEqual(self.varasto.saldo, 10)
        
    def test_varastoon_poista_liikaa_tavaraa(self):
        varastossa_tilaa = self.varasto.paljonko_mahtuu()
        self.varasto.lisaa_varastoon(varastossa_tilaa)
        self.varasto.ota_varastosta(varastossa_tilaa)
        self.varasto.ota_varastosta(1)
        self.assertAlmostEqual(self.varasto.saldo, 0)
        
    def test_ota_varastota_negatiivinen_maara(self):
        varastossa_tilaa = self.varasto.paljonko_mahtuu()
        self.varasto.lisaa_varastoon(varastossa_tilaa)

        vastaus = self.varasto.ota_varastosta(-varastossa_tilaa)
        self.assertEqual(vastaus, 0)

    def test_lisaa_varastoon_negatiivinen(self):
        varastossa_tilaa = self.varasto.paljonko_mahtuu()
        self.varasto.lisaa_varastoon(-varastossa_tilaa)
        self.assertEqual(varastossa_tilaa, varastossa_tilaa)

    def test_luodaan_varasto_negatiivinen_tilavuus(self):
        varasto = Varasto(-10)
        self.assertEqual(varasto.tilavuus, 0)

    def test_luodaan_varasto_negatiivinen_saldo(self):
        varasto = Varasto(10, -1)
        self.assertEqual(varasto.saldo, 0)

    def test_varasto_str(self):
        s = str(self.varasto)
        self.varasto.saldo = 0
        mahtuu = self.varasto.paljonko_mahtuu()
        vastaus = "saldo = 0, vielä tilaa " + str(mahtuu)
        self.assertEqual(s, vastaus)