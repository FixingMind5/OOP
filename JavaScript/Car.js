class Car {
  constructor(license, driver) {
    this.id;
    this.license = license;
    this.driver = driver;
    this.passenger;
  }

  print_data_car() {
    console.log(this.driver);
    console.log(this.driver.name);
    console.log(this.driver.document);
    console.log(this.license);
  }
}
