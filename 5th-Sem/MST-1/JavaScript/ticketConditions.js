// 3.d Conditions and switch example
function bookTickets(seats) {
  const price = 150;
  if (seats <= 2) return seats * price;
  if (seats >= 6) return 'Booking not allowed';
  // seats 3-5 apply incremental discounts 3%,5%,7%
  const discounts = [0.03,0.05,0.07];
  const idx = seats - 3;
  const total = seats * price;
  const discount = total * discounts[idx] || 0;
  return total - discount;
}
console.log(bookTickets(4));
