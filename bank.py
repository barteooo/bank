from account import Account
from apperance import Apperance
from iban_generator import generate_iban
from options import Options
from transaction import Transaction


class LoginAlreadyExists(Exception):
    pass


class PhoneNumberAlreadyExistsException(Exception):
    pass


class Bank:
    def __init__(self):
        self.accounts = [Account("barteoo","Bartłomiej","Wnuk", "532492751",  "1010101010101010101010", "haslo"),
                         Account("jaszke", "Grzegorz", "Formela", "121235657","9999999999999999999999", "haslo")]
        self.options = Options(self)
        self.account = None

    def create_account(self):
        login = self.get_input(self.options.login_creator, "Wpisz login")
        print("login został utworzony")
        imie = self.get_input(self.options.name_validator, "Wpisz imie")
        print("imię zostało zatwierdzone")
        nazwisko = self.get_input(self.options.surname_validator, "Wpisz nazwisko")
        print("nazwisko zostało zatwierdzone")
        phone = self.get_input(self.options.phone_validator, "Wpisz numer telefonu")
        print("telefon został zatwierdzony")
        password = input("Podaj hasło: ")
        print("hasło zostało utworzone")
        iban = generate_iban(self.accounts)
        print(f"iban został pomyślnie utworzony i wynosi: {iban}.Zapisz go!")
        self.accounts.append(Account(login,imie,nazwisko,phone,iban,password))
        print("Twoje konto zostało pomyślnie utworzone!")


    def get_input(self, func, prompt):
        while True:
            try:
                text = input(prompt)
                result = func(text)
                return result
            except Exception as e:
                print(e)
                continue

    def login_account(self):
        while True:
            try:
                login = input("Podaj login: ")
                password = input("Podaj haslo: ")
                self.account = self.options.login(login, password)
                return
            except Exception as e:
                print(e)

    def logged_menu(self):
        while True:
            Apperance.logged_menu()
            option = input("Podaj numer opcji: ")
            try:
                if option == '1':
                    self.account.deposit()
                elif option == '2':
                    self.account.withdraw()
                elif option == "3":
                    self.account.data_information()
                elif option == '4':
                    self.account.transfer_money(self)
                elif option == '5':
                    self.account.extract_transactions()
                elif option == "6":
                    self.account = None
                    return
                else:
                    raise ValueError("Niepoprawna opcja")
            except ValueError as error:
                print(error)

    def no_logged_menu(self):
        while True:
            Apperance.no_logged_menu()
            option = input("Podaj numer opcji: ")
            try:
                if option == '1':
                    self.create_account()
                elif option == '2':
                    self.login_account()
                    self.logged_menu()
                else:
                    raise ValueError("Niepoprawna opcja")

            except ValueError as error:
                print(error)

    def transfering_money(self,transaction,sender):
        if not self.options.if_iban_exists(self.accounts,transaction.destination_account):
            print("transakcja się nie powiodła! Podany przez ciebie numer konta Iban jest niepoprawny!!!")
        elif transaction.destination_account == transaction.source_account:
            print("transakcja się nie powiodła! Nie możesz zrobić przelewu na własne konto")
        else:
            sender.get_transfer(transaction)
            transaction_with_new_type = Transaction(transaction.amount, "Przelew wchodzący", transaction.description, transaction.source_account, transaction.destination_account)
            receiver_account = self.option.search_account_by_iban(self.accounts,transaction.destination_account)
            receiver_account.give_transfer(transaction_with_new_type)







