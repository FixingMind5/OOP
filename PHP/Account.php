<?php

class Account {
  public $id;
  public $document;
  public $name;
  public $email;
  public $password;

  public function __construct($name, $document) {
    $this->name = $name;
    $this->document = $document;
  }
}

?>
