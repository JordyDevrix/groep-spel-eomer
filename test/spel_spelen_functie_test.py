import unittest
import tkinter as tk
from unittest.mock import patch

# Importeer de functies die we willen testen
from groep_12_eomer/spel_spelen_functie.py import main, tijd_locatie_weergeven


class TestMijnCode(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()

    def tearDown(self):
        self.root.destroy()

    def test_main(self):
        with patch("builtins.input", return_value="Rivendel"):
            main(self.root)

        widgets = self.root.winfo_children()
        button_tl = widgets[0]

        self.assertEqual(button_tl.cget("text"), "Tijd/Locatie")

    def test_tijd_locatie_weergeven(self):
        tijd = "10:12"
        locatie = "Rivendel"

        tijd_locatie_weergeven(self.root)

        widgets = self.root.winfo_children()
        frame1 = widgets[0]
        lt_label = frame1.winfo_children()[0]

        self.assertEqual(lt_label.cget("text"), f"{tijd} en {locatie}")


if __name__ == '__main__':
    unittest.main()