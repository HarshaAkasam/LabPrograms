// 11.b Create objects of Product class
class ProductClass {
  constructor(public id:number, public name:string) {}
}
const productList = [ new ProductClass(1,'P1'), new ProductClass(2,'P2') ];
console.log(productList);
