class LoginAlreadyExists(Exception):
    pass

class PhoneNumberAlreadyExistsException(Exception):
    pass

class PhoneNumberWrongLength(Exception):
    pass

class PhoneNumberContainsLetters(Exception):
    pass

class FirstLetterIsNotBig(Exception):
    pass

class WrongLength(Exception):
    pass

class NoLoginInSystem(Exception):
    pass

class InvalidPassword(Exception):
    pass


class IbanIsWrong(Exception):
    pass

class IbanHasLetters(Exception):
    pass

class AmountIsTooLow(Exception):
    pass

class AmountIsTooBig(Exception):
    pass

class WrongTypeOfAmount(Exception):
    pass


class Options:
    def __init__(self, bank):
        self.accounts = bank.accounts

    def login_creator(self, login):
        if any(a for a in self.accounts if a.login == login):
            raise LoginAlreadyExists("Konto o podanym loginie już istnieje")
        else:
            return login

    def phone_validator(self, phone_number):
        if any(a for a in self.accounts if a.phone_number == phone_number):
            raise PhoneNumberAlreadyExistsException("Podany numer telefonu jest przypisany do innego konta")
        if len(phone_number) != 9:
            raise PhoneNumberWrongLength("Numer telefonu musi mieć 9 cyfr")
        if not phone_number.isdigit():
            raise PhoneNumberContainsLetters("Numer telefonu nie może zawierać liter")
        else:
            return phone_number

    def name_validator(self, name):
        if not name[0].isupper():
            raise FirstLetterIsNotBig("Pierwsza litera imienia musi być dużym znakiem")
        if not len(name) >= 3:
            raise WrongLength("Imię musi mieć więcej niż trzy znaki")
        else:
            return name

    def surname_validator(self, surname):
        if not surname[0].isupper():
            raise FirstLetterIsNotBig("Pierwsza litera nazwiska musi być dużym znakiem")
        if not len(surname) >= 3:
            raise WrongLength("Nazwisko musi mieć więcej niż trzy znaki")
        else:
            return surname

    def login(self, login, password):
        if not any(a for a in self.accounts if a.login == login):
            raise NoLoginInSystem("Nie ma użytkownika o podanym loginie")
        account = next((a for a in self.accounts if a.login == login), None)
        if account.password != password:
            raise InvalidPassword("Niepoprawne hasło")
        else:
            return account

    def IbanCheck(self, account):
        try:
            if len(account) != 22:
                raise IbanIsWrong("Numer Iban musi mieć 22 cyfry")
            if not account.isdigit():
                raise IbanHasLetters("Iban nie może zawierać liter")
            else: return True
        except IbanIsWrong as error:
            print(error)
        except IbanHasLetters as error:
            print(error)

    def amount_validator(self, ammount):
        try:
            float(ammount)
            return True
        except ValueError:
            print("Kwota może się składać z samych cyfr i ewentualnej kropki")
            return False

    def if_iban_exists(self, accounts, receiver):
        return any(a.iban == receiver for a in accounts)

    def search_account_by_iban(self, accounts, iban):
        account = next((a for a in accounts if a.iban == iban), None)
        return account


