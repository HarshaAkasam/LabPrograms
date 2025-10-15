// 9.b Arrow function inside event handler to filter product array
type Product = { productId:number, name:string };
const products: Product[] = [{productId:1,name:'A'},{productId:2,name:'B'}];
function onSelect(productId:number){
  const selected = products.filter(p=>p.productId===productId)[0];
  console.log('Selected', selected);
}
onSelect(2);
