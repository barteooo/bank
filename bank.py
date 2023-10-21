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
                         Account("jaszke", "Grzegorz", "Formela", "121235657","9999999999999999999999", "haslo")
                         ]

    def create_account(self):
        login = Options.login_creator(self.accounts)
        print("login został utworzony")
        imie = Options.name_validator()
        print("imię zostało zatwierdzone")
        nazwisko = Options.surname_validator()
        print("nazwisko zostało zatwierdzone")
        phone = Options.phone_validator(self.accounts)
        print("telefon został zatwierdzony")
        password = input("Podaj hasło: ")
        print("hasło zostało utworzone")
        iban = generate_iban(self.accounts)
        print(f"iban został pomyślnie utworzony i wynosi: {iban}.Zapisz go!")
        self.accounts.append(Account(login,imie,nazwisko,phone,iban,password))
        print("Twoje konto zostało pomyślnie utworzone!")


    def login_account(self):
        account = Options.login(self.accounts)
        Apperance.logged_menu()
        while True:
            option = input("Podaj numer opcji: ")
            try:
                if option == '1':
                    Account.deposit(account)
                elif option == '2':
                    Account.withdraw(account)
                elif option == "3":
                    Account.data_information(account)
                elif option == '4':
                    Account.transfer_money(account,self)
                elif option == '5':
                    Account.extract_transactions(account)
                elif option == "6":
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
                else:
                    raise ValueError("Niepoprawna opcja")

            except ValueError as error:
                print(error)

    def transfering_money(self,transaction,sender):
        if not Options.if_iban_exists(self.accounts,transaction.destination_account):
            print("transakcja się nie powiodła! Podany przez ciebie numer konta Iban jest niepoprawny!!!")
        elif transaction.destination_account == transaction.source_account:
            print("transakcja się nie powiodła! Nie możesz zrobić przelewu na własne konto")
        else:
            sender.get_transfer(transaction)
            transaction_with_new_type = Transaction(transaction.amount, "Przelew wchodzący", transaction.description, transaction.source_account, transaction.destination_account)
            receiver_account = Options.search_account_by_iban(self.accounts,transaction.destination_account)
            receiver_account.give_transfer(transaction_with_new_type)







