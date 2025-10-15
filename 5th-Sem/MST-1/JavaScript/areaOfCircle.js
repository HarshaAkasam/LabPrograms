// 3.a Type of Identifiers - area of circle demo
const PI = 3.141592653589793;
function areaVarRadius() {
  var radius = 5;
  radius = 7; // var can be reassigned
  return PI * radius * radius;
}
let areaLetRadius = function() {
  let radius = 5;
//  radius = 8; // let can be reassigned too
  return PI * radius * radius;
};
console.log('areaVarRadius()', areaVarRadius());
console.log('areaLetRadius()', areaLetRadius());
