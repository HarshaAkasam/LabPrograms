// 10.a Rest parameter example
function addToCart(...products:string[]) {
  const cart:string[] = [];
  cart.push(...products);
  return cart;
}
console.log(addToCart('p1','p2','p3'));
