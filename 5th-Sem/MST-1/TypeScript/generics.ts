// 12.d Generic sort function
function sortItems<T>(arr:T[]):T[] {
  return arr.slice().sort();
}
console.log(sortItems<number>([3,1,2]));
console.log(sortItems<string>(['b','a','c']));
