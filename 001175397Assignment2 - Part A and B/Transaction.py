class Transaction:
    def __init__(self, date, barcode, amount):
        self.date = date
        self.barcode = barcode
        self.amount = amount

    def __str__(self):
        return f"Date: {self.date}, Barcode: {self.barcode}, Amount: {self.amount}"

    def get_date(self):
        return self.date

    def get_barcode(self):
        return self.barcode

    def get_amount(self):
        return self.amount
