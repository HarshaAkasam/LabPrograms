// 5.a Array of movie objects and render
const movies = [
  {name:'Alpha', starring:['A','B'], language:'English', ratings:4.2},
  {name:'Beta', starring:['C','D'], language:'Hindi', ratings:4.6}
];
if (typeof document !== 'undefined') {
  const ul = document.createElement('ul');
  movies.forEach(m=>{
    const li = document.createElement('li');
    li.textContent = `${m.name} - ${m.language} - ${m.ratings}`;
    ul.appendChild(li);
  });
  document.body.appendChild(ul);
} else {
  console.log(movies);
}
