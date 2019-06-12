from payment import Payment

class Card(Payment):
    number = int
    cvv = int
    date = str

    def __init__(self, id, number, cvv, date):
        super().__init__(id)
        self.number = number
        self.cvv = cvv
        self.date = date

    def print_data_card(self):
        print("Number card {} \nCVV: {}\nDate: {}".format(self.number, self.cvv, self.date))
