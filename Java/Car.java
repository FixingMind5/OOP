class Car {
  Integer id;
  String license;
  Account driver;
  private Integer passenger;

  public Car(String license, Account driver) {
    this.license = license;
    this.driver = driver;
  }

  void print_data() {
    System.out.println("License: " + license + ", Driver name: " + driver.name);
  }

  public Integer get_passenger() {
    return  passenger;
  }

  public void set_passenger(Integer passenger) {
    if (passenger == 4) {
      this.passenger = passenger;
      System.out.println("Pasajeros asignados");
    } else {
      System.out.println("Necesitas asignar 4 pasajeros");
    }
  }
}
