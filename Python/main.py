from car import Car

if __name__ == '__main__':
    print("Hello world!")

    car = Car()
    car.id = 1234
    car.license = "AMQ123"
    car.driver = "Andrés Herrera"

    print("License: {}, Driver: {} ".format(car.license, car.driver))
    # print(vars(car)) Con esto podemos imprimir todo lo que esté dentro de esa varible
