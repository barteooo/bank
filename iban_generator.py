import random


def generate_iban(accounts):
    while True:
        iban = "PL" + str(random.randint(1, 10**20)).zfill(20)
        if not any(a for a in accounts if a.iban == iban):
            return iban