class Payment:
    def __init__(self, total):
        self.total = total

    def __str__(self):
        return f'Payment total is {self.total}'


class Credit(Payment):
    def __init__(self, total, number, exp_date):
        super().__init__(total)
        self.number = number
        self.exp_date = exp_date

    def __str__(self):
        return f'Credit payment total is {self.total}'


class Check(Payment):
    def __init__(self, total, number, bank_code):
        super().__init__(total)
        self.number = number
        self.bank_code = bank_code

    def __str__(self):
        return f'Check payment total is {self.total}'


