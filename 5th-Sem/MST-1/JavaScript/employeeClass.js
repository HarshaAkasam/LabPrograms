// 4.b Classes and inheritance
class Person {
  constructor(name, age){ this.name=name; this.age=age; }
}
class Employee extends Person {
  constructor(name, age, role, contact){
    super(name, age);
    this.role = role;
    this.contact = contact;
  }
  getDetails(){ return `${this.name} (${this.age}) - ${this.role} - ${this.contact}`; }
}
const e = new Employee('Ravi',28,'Developer','9999999999');
console.log(e.getDetails());
