<?php

require_once("Car.php");

class UberBlack extends Car {
  public $typeCar;
  public $seatsMaterial;

  public function __construct($license, $driver, $typeCar, $seatsMaterial) {
    parent::__construct($license, $driver);

    $this->typerCar = $typeCar;
    $this->seatsMaterial = $seatsMaterial;
  }
}

?>
