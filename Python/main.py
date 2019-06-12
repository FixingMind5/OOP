from car import Car
from account import Account

if __name__ == '__main__':
    print("Hello world!")

    andrew = Account("Andrew Herrera", "AGH23")
    car = Car("AMG34", andrew)

    car.print_data_car()

    # print(vars(car)) Con esto podemos imprimir todo lo que esté dentro de esa varible
