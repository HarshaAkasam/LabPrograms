// 4.a Arrow functions and nested functions
const price = 150;
const calculateDiscount = (seats) => {
  if (seats <= 2) return 0;
  const percents = [3,5,7,9,11]; // percent for customers
  return (percents[seats-3] || 0) / 100;
};
const calculateCost = (seats) => {
  const total = seats * price;
  const disc = calculateDiscount(seats);
  return total - (total * disc);
};
// expose for modules
if (typeof window !== 'undefined') window.calculateCost = calculateCost;
console.log(calculateCost(4));
