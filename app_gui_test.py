import unittest
from tkinter import Tk
from unittest.mock import patch
from app_gui import menu, settings

class TestApp(unittest.TestCase):
    @patch("your_module_name.character_maken")
    def test_menu(self, mock_character_maken):
        root = Tk()
        menu(root)
        menu_buttons = root.winfo_children()[1].winfo_children()[0].winfo_children()

        # Controleer of de CREATE A CHARACTER-knop werkt
        menu_buttons[0].invoke()
        mock_character_maken.assert_called_with(root, menu)

    def test_settings(self):
        root = Tk()
        settings(root)

        # Voeg hier verificatie toe om te controleren of de instellingen worden weergegeven zoals verwacht

if __name__ == "__main__":
    unittest.main()
