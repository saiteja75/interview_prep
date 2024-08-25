// Super Class
class FactoryMethod {
  constructor() {}

  genericMethod() {}
}

// Child Class 1
class ChildOne extends FactoryMethod {
  constructor() {}

  genericMethod() {
    console.log('genericMethod in the child one');
  }
}

// Child Class 2
class ChildTwo extends FactoryMethod {
  constructor() {}

  genericMethod() {
    console.log('genericMethod in the child two');
  }
}
