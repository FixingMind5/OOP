from car import Car
from account import Account
from uberBlack import UberBlack

if __name__ == '__main__':
    print("Hello world!")

    uberBlack = UberBlack(
                        "ANG23",
                        Account("Andrés Herrera", "MDN45"),
                        "Mercedez Benz",
                        "20018")

    print(vars(uberBlack))

    # print(vars(car)) Con esto podemos imprimir todo lo que esté dentro de esa varible
