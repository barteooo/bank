from transaction import Transaction
from datetime import datetime
from options import Options



class AmountIsToLow(Exception):
    pass

class Account:
    def __init__(self,login,imie,nazwisko,phone_number,iban,password) -> None:
        self.login = login
        self.imie = imie
        self.nazwisko = nazwisko
        self.phone_number = phone_number
        self.iban = iban
        self.password = password
        self.balance = 10
        self.history = []

    def data_information(self):
        print(f"Witaj: {self.login}")
        print(f"iban: {self.iban}")
        print(f"saldo: {self.balance}")
        print(f"wykaz operacji: {self.history} ")

    def deposit(self):
        amount = input("Podaj kwotę jaką chcesz wpłacić: ")
        self.balance += int(amount)
        self.history.append(Transaction(amount, "Wpłata", "Wpłata na konto"))
        print(f"Wpłacono {amount}")

    def withdraw(self):
        amount = input("Podaj kwotę jaką chcesz wypłacić: ")
        try:
            if int(amount) > self.balance:
                raise ValueError("Niewystarczjąca ilość środków na koncie")
            else:
                self.balance -= int(amount)
                self.history.append(Transaction(amount, "Wypłata", "Wypłata z konta"))
                print(f"Wypłacono {amount}")
        except ValueError as error:
            print(error)

    def transfer_money(self,bank):
        while True:
            receiver = input("Podaj numer IBAN odbiorcy:  ")
            if(bank.options.IbanCheck(receiver)):
                break;
        tittle = input("Podaj tytuł przelewu: ")
        while True:
            amount = input("Podaj kwotę przelewu: ")
            if bank.options.amount_validator((amount)):
                break;
        try:
            if float(amount) > self.balance:
                raise ValueError("Niewystarczjąca ilość środków na koncie. Przelew nie został dokonany")
            else:
                bank.transfering_money(Transaction(amount,"Przelew wychodzący",tittle,self.iban,receiver),self)

        except ValueError as error:
            print(error)

    def get_transfer(self,transaction):
        self.history.append(transaction)
        self.balance -= float(transaction.amount)

    def give_transfer(self,transaction):
        self.history.append(transaction)
        self.balance += float(transaction.amount)

    def extract_transactions(self):
        while True:
            try:
                start_date_str = input("Podaj datę początkową w formacie YYYY-MM-DD: ")
                start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
                end_date_str = input("Podaj datę końcową w formacie YYYY-MM-DD: ")
                end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
                break
            except ValueError:
                print("Błędny format daty! Spróbuj ponownie.")
        extracted_transactions = [trans for trans in self.history if start_date.date() <= trans.timestamp.date() <= end_date.date()]
        for trans in extracted_transactions:
            print(trans)
        return extracted_transactions


























































