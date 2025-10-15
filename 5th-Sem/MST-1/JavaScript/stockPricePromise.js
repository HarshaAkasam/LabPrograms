// 5.b Simulate periodic stock price change using Promise and setInterval
function getRandomPrice() {
  return Math.floor(100 + Math.random()*50);
}
function simulatePrices() {
  return new Promise((resolve)=>{
    let count=0;
    const prices=[];
    const id = setInterval(()=>{
      count++;
      const p=getRandomPrice();
      console.log('Price', count, p);
      prices.push(p);
      if (count>=5) {
        clearInterval(id);
        resolve(prices);
      }
    },3000);
  });
}
simulatePrices().then(res=>console.log('Done', res));
