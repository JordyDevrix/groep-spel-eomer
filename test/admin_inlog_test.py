import unittest
from tkinter import Tk
from admin_inloggen import admin_inlogscherm, admin_scherm, verhaal_1, verhaal_2, verhaal_3

class TestGUIApp(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.root.geometry("800x600")

    def test_admin_login_success(self):
        admin_inlogscherm(self.root, lambda root: None)
        username_entry = self.root.children['!frame'].children['!frame'].children['!entry']
        password_entry = self.root.children['!frame'].children['!entry2']
        login_button = self.root.children['!frame'].children['!button']
        username_entry.insert(0, "admin_username")
        password_entry.insert(0, "admin_password")
        login_button.invoke()
        self.assertNotIn('login_frame', self.root.children)

    def test_admin_login_fail(self):
        admin_inlogscherm(self.root, lambda root: None)
        username_entry = self.root.children['!frame'].children['!frame'].children['!entry']
        password_entry = self.root.children['!frame'].children['!entry2']
        login_button = self.root.children['!frame'].children['!button']
        username_entry.insert(0, "admin_username")
        password_entry.insert(0, "wrong_password")
        login_button.invoke()
        self.assertIn('login_frame', self.root.children)

    def test_navigation_between_screens(self):
        admin_scherm(self.root, lambda root: None)
        admin_verhaal1_button = self.root.children['!frame'].children['!button']
        admin_verhaal1_button.invoke()
        self.assertNotIn('admin_frame', self.root.children)

        verhaal_1(self.root, lambda root: None)
        verhaal_verhaal2_button = self.root.children['!frame'].children['!button']
        verhaal_verhaal2_button.invoke()
        self.assertNotIn('verhaal_frame', self.root.children)

    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()
