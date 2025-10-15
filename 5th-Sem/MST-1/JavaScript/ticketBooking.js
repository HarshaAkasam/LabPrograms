// 3.c Operators - calculate total price with discount
const pricePerTicket = 150;
function calculateTotal(tickets) {
  let total = tickets * pricePerTicket;
  let discount = 0;
  if (tickets > 2 && tickets < 6) {
    // 10% festive discount for example
    discount = total * 0.1;
  }
  return { total, discount, payable: total - discount };
}
console.log(calculateTotal(3));
