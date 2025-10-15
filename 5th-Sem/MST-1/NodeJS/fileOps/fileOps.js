// 6.e File operations - read src.txt
const fs = require('fs');
const path = require('path');
const p = path.join(__dirname,'src.txt');
fs.readFile(p,'utf8',(err,data)=>{
  if (err) return console.error(err);
  console.log('src.txt contents:', data);
});
