import unittest
from unittest.mock import MagicMock
from tkinter import Tk, Frame, Button, Entry, Label
from character_maken import character_maken, naam_ophalen, ras_kiezen, ras_binnen_krijgen, character_gegevens_wegschrijven

class TestCharacterFunctions(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.venster = Frame(self.root)
        self.menu_mock = MagicMock()

    def tearDown(self):
        self.root.destroy()

    def test_character_maken(self):
        result = character_maken(self.venster, self.menu_mock)
        self.assertIsInstance(result, Frame)
        self.assertEqual(len(self.venster.winfo_children()), 2)

    def test_naam_ophalen(self):
        name_input = Entry(self.venster)
        name_input.insert(0, "John Doe")
        naam_ophalen(self.venster, name_input, self.menu_mock)
        label_huidige_naam = self.venster.winfo_children()[-2]
        self.assertEqual(label_huidige_naam.cget("text"), "Uw huidige naam: John Doe")

    def test_ras_kiezen(self):
        ras_kiezen(self.venster, self.menu_mock, "John Doe")
        self.assertEqual(len(self.venster.winfo_children()), 9)

    def test_ras_binnen_krijgen(self):
        ras_binnen_krijgen(self.venster, 1, self.menu_mock, "John Doe")
        self.assertEqual(len(self.venster.winfo_children()), 3)

    def test_character_gegevens_wegschrijven(self):
        character_gegevens_wegschrijven("sterk", "John Doe")


if __name__ == '__main__':
    unittest.main()
