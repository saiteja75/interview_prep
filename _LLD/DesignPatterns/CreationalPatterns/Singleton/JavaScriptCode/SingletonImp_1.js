class SingleTon {
  static __instance = null;
  counter = 0;

  constructor() {
    if (SingleTon.__instance) {
      return SingleTon.__instance;
    }
    SingleTon.__instance = this;
  }

  sampleMethod() {
    this.counter += 1;
    console.log('Test');
  }
}

let s1 = new SingleTon();
let s2 = new SingleTon();
s1.sampleMethod();
s2.sampleMethod();
console.log(s1 === s2);
console.log(s1.counter, s2.counter);
export default s1;
