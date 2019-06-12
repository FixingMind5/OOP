from car import Car
from account import Account
from uberBlack import UberBlack
from payment import Payment
from card import Card

if __name__ == '__main__':
    print("Hello world!")

    """uberBlack = UberBlack(
                        "ANG23",
                        Account("Andrés Herrera", "MDN45"),
                        "Mercedez Benz",
                        "20018")

    print(vars(uberBlack))"""

    newCard = Card("01", "4554-8584-02834-2837", "344", "2032-05-03")
    newCard.print_data_card()

    # print(vars(car)) Con esto podemos imprimir todo lo que esté dentro de esa varible
