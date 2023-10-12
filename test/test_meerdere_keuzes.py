import unittest
from unittest.mock import patch
import tempfile
import tkinter as tk
import json

from meerdere_keuzes import lees_gegevens, update_interface, kies_optie, start_tekst_avontuur


class TestTextAdventure(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.bestand = None  # We gebruiken een tijdelijk bestand voor de test

    def tearDown(self):
        self.root.destroy()

    def create_temp_json(self, data):
        # Creëer een tijdelijk JSON-bestand voor de test
        with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
            temp_file.write(json.dumps(data))
            self.bestand = temp_file.name

    @patch("tkinter.Label.config")
    def test_update_interface(self, mock_label_config):
        gegevens = {
            "locaties": {
                "start": {"beschrijving": "Dit is het begin", "keuzes": [{"Keuze 1": "locatie1"}]}
            }
        }

        beschrijving_label = tk.Label(self.root)
        button_frame = tk.Frame(self.root)

        huidige_locatie = "start"
        update_interface(huidige_locatie, gegevens, beschrijving_label, button_frame)

        # Haal de opgeroepen argumenten op
        call_args = mock_label_config.call_args[0][0]

        # Test of de tekst op het label correct is bijgewerkt
        self.assertEqual(call_args["text"], gegevens["locaties"]["start"]["beschrijving"])

        # Test of de knoppen correct zijn gegenereerd
        self.assertEqual(len(button_frame.winfo_children()), len(gegevens["locaties"]["start"]["keuzes"]))

    @patch("tkinter.Label.config")
    @patch("tkinter.Button.destroy")
    def test_kies_optie(self, mock_button_destroy, mock_label_config):
        gegevens = {
            "locaties": {
                "start": {"beschrijving": "Dit is het begin", "keuzes": [{"Keuze 1": "locatie1"}]},
                "locatie1": {"beschrijving": "Dit is locatie 1", "keuzes": []}
            }
        }

        beschrijving_label = tk.Label(self.root)
        button_frame = tk.Frame(self.root)

        huidige_locatie = "start"
        update_interface(huidige_locatie, gegevens, beschrijving_label, button_frame)

        # Simuleer het kiezen van een optie
        kies_optie("locatie1", huidige_locatie, gegevens, beschrijving_label, button_frame)

        # Verifieer of de mock-functies correct zijn opgeroepen
        mock_label_config.assert_called_with({"text": "Dit is het begin"})
        self.assertEqual(mock_button_destroy.call_count, len(gegevens["locaties"]["start"]["keuzes"]))


if __name__ == '__main__':
    unittest.main()








