import unittest
from bank import *
from options import *

class OptionsTest(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()
        self.bank.accounts.append(Account("test","Bartłomiej","Wnuk", "999999999",  "1010101010101010101010", "haslo"))
        self.options = self.bank.options

    def test_login_creator(self):
        with self.assertRaises(LoginAlreadyExists):
            self.options.login_creator("test")
        self.assertEqual(self.options.login_creator("newuser"), "newuser")

    def test_phone_validator(self):
        with self.assertRaises(PhoneNumberAlreadyExistsException):
            self.options.phone_validator("999999999")

        with self.assertRaises(PhoneNumberWrongLength):
            self.options.phone_validator("12345")

        with self.assertRaises(PhoneNumberContainsLetters):
            self.options.phone_validator("12345678a")

        self.assertEqual(self.options.phone_validator("987654321"), "987654321")

    def test_name_validator(self):
        with self.assertRaises(FirstLetterIsNotBig):
            self.options.name_validator("john")

        with self.assertRaises(WrongLength):
            self.options.name_validator("Jo")

        self.assertEqual(self.options.name_validator("John"), "John")

    def test_surname_validator(self):
        with self.assertRaises(FirstLetterIsNotBig):
            self.options.name_validator("john")

        with self.assertRaises(WrongLength):
            self.options.name_validator("Jo")
        self.assertEqual(self.options.name_validator("John"), "John")

    def test_login(self):
        # Testing login with a non-existent username
        with self.assertRaises(NoLoginInSystem):
            self.options.login("nonexistentuser", "randompassword")

        # Testing login with a correct username but incorrect password
        with self.assertRaises(InvalidPassword):
            self.options.login("test", "wrongpassword")

        # Testing login with correct credentials
        account = self.options.login("test", "haslo")
        self.assertEqual(account.login, "test")
        self.assertEqual(account.password, "haslo")

    def test_amount_validator(self):
        # Test valid amount
        self.assertTrue(self.options.amount_validator("123.45"))

        # Test valid amount without decimals
        self.assertTrue(self.options.amount_validator("123"))

        # Test invalid amount with letters
        with self.subTest(msg="Testing amount with letters"):
            self.assertFalse(self.options.amount_validator("123a.45"))

        # Test invalid amount with multiple dots
        with self.subTest(msg="Testing amount with multiple dots"):
            self.assertFalse(self.options.amount_validator("123..45"))

        # Test invalid format
        with self.subTest(msg="Testing amount with comma instead of dot"):
            self.assertFalse(self.options.amount_validator("123,45"))
