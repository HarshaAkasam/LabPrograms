// 4.c Events - invoke discount calculation on button click
document.addEventListener('DOMContentLoaded', ()=>{
  const btn = document.createElement('button');
  btn.textContent = 'Calculate Cost for 4 seats';
  btn.addEventListener('click', ()=>{
    const payable = window.calculateCost ? window.calculateCost(4) : 'See console';
    alert('Payable: ' + payable);
  });
  document.body.appendChild(btn);
});
