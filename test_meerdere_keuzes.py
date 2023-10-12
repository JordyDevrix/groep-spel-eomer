import unittest
from unittest.mock import patch
import tkinter as tk
from meerdere_keuzes import lees_gegevens, update_interface, kies_optie, start_tekst_avontuur


class TestTextAdventure(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.bestand = "test_data.json"

    def tearDown(self):
        self.root.destroy()

    @patch("tkinter.Label.config")
    def test_update_interface(self, mock_label_config):
        gegevens = lees_gegevens(self.bestand)
        beschrijving_label = tk.Label(self.root)
        button_frame = tk.Frame(self.root)

        huidige_locatie = "start"
        update_interface(huidige_locatie, gegevens, beschrijving_label, button_frame)

        # Test of de beschrijving correct is bijgewerkt
        self.assertEqual(mock_label_config.call_args[0][0], {"text": gegevens["locaties"]["start"]["beschrijving"]})

        # Test of de knoppen correct zijn gegenereerd
        self.assertEqual(len(button_frame.winfo_children()), len(gegevens["locaties"]["start"]["keuzes"]))


if __name__ == '__main__':
    unittest.main()
