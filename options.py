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
    def login_creator(accounts):
        while True:
            try:
                login = input("Podaj login: ")
                if any(a for a in accounts if a.login == login):
                    raise LoginAlreadyExists("Konto o podanym loginie już istnieje")
                else:
                    return login
            except LoginAlreadyExists as error:
                print(error)


    def phone_validator(accounts):
        while True:
            try:
                phone_number = input("Podaj numer telefonu: ")
                if any(a for a in accounts if a.phone_number == phone_number):
                    raise PhoneNumberAlreadyExistsException("Podany numer telefonu jest przypisany do innego konta")
                if len(phone_number) != 9:
                    raise PhoneNumberWrongLength("Numer telefonu musi mieć 9 cyfr")
                if not phone_number.isdigit():
                    raise PhoneNumberContainsLetters("Numer telefonu nie może zawierać liter")
                else:
                    return phone_number
            except PhoneNumberAlreadyExistsException as error:
                print(error)
            except PhoneNumberWrongLength as error:
                print(error)
            except PhoneNumberContainsLetters as error:
                print(error)

    def name_validator():
        while True:
            try:
                name = input("Podaj imię: ")
                if not name[0].isupper():
                    raise FirstLetterIsNotBig("Pierwsza litera imienia musi być dużym znakiem")
                if not len(name) >= 3:
                    raise WrongLength("Imię musi mieć więcej niż trzy znaki")
                else:
                    return name
            except FirstLetterIsNotBig as error:
                print(error)
            except WrongLength as error:
                print(error)


    def surname_validator():
        while True:
            try:
                nazwisko = input("Podaj Nazwisko: ")
                if not nazwisko[0].isupper():
                    raise FirstLetterIsNotBig("Pierwsza litera nazwiska musi być dużym znakiem")
                if not len(nazwisko) >= 3:
                    raise WrongLength("Nazwisko musi mieć więcej niż trzy znaki")
                else:
                    return nazwisko
            except FirstLetterIsNotBig as error:
                print(error)
            except WrongLength as error:
                print(error)


    def login(accounts):
        while True:
            try:
                login_input = input("Podaj login: ")
                if not any(a for a in accounts if a.login == login_input):
                    raise NoLoginInSystem("Nie ma użytkownika o podanym loginie")
                password_input = input("Podaj hasło: ")
                account = next((a for a in accounts if a.login == login_input), None)
                if account.password != password_input:
                    raise InvalidPassword("Niepoprawne hasło")
                else:
                    return account

            except NoLoginInSystem as error:
                print(error)
            except InvalidPassword as error:
                print(error)


    def IbanCheck(account):
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


    def amount_validator(ammount):
        try:
            float(ammount)
            return True
        except ValueError:
            print("Kwota może się składać z samych cyfr i ewentualnej kropki")

    def if_iban_exists(accounts, receiver):
        return any(a.iban == receiver for a in accounts)


    def search_account_by_iban(accounts, iban):
        account = next((a for a in accounts if a.iban == iban), None)
        return account


