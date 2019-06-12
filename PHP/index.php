<?php
require_once("Car.php");
require_once("UberX.php");
require_once("Account.php");


$uberX = new UberX("CVB132", new Account("Andrés Herrera", "AND13"), "Chevrolet", "Spark");
$uberX->print_data_car();

?>
