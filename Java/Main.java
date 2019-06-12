class Main {
  public static void main(String[] args) {
    System.out.println("Hello World");

    Car car = new Car(); //This the way how we initialize a new Object
    car.id = 123456; //Now we're entering to an attribute of class Car
    car.license = "AMQ123";
    car.driver = "Andrés Herrera";
    car.passenger = 4;

    //Printing our attributes
    System.out.println("Car license: " + car.license);
    System.out.println("Car driver: " + car.driver);

    //Declaring another instance of class Car
    Car andreaCar = new Car();
    andreaCar.license = "AMH123";
    andreaCar.driver = "Andrea Herrera";

    andreaCar.print_data();
    car.print_data();
  }
}
