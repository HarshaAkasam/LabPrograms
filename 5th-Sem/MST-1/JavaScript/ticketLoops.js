// 3.e Loops implementation: for, while, do-while
function calcFor(n) {
  for (let i=1;i<=n;i++) console.log('For loop customer', i);
}
function calcWhile(n) {
  let i=1; while(i<=n){ console.log('While loop customer', i); i++;}
}
function calcDoWhile(n) {
  let i=1; do{ console.log('Do-While customer', i); i++; } while(i<=n);
}
calcFor(3); calcWhile(2); calcDoWhile(1);
