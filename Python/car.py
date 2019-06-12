from account import Account

class Car:
    id = int
    license = str
    driver = Account
    passenger = str

    def __init__(self, license, driver):
        self.license = license
        self.driver = driver


    def print_data_car(self):
        print("License: {}, Name: {}, Documet: {}".format(self.license, self.driver.name, self.driver.document))
