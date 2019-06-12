class Main {
  public static void main(String[] args) {
    System.out.println("Hello World");

    Account andres = new Account("Andrés Herrera", "Driver");
    Car car = new Car("AMQ123", andres); //This the way how we initialize a new Object
    car.id = 123456; //Now we're entering to an attribute of class Car

    //Printing our attributes
    /*
    System.out.println("Car license: " + car.license);
    System.out.println("Car driver: " + car.driver);
    */

    //Declaring another instance of class Car
    Car andreaCar = new Car("AMH123", new Account("Andrea Herrera", "Driver"));

    andreaCar.print_data();
    car.print_data();
  }
}
