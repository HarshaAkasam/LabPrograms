import { User } from './login.js';
document.addEventListener('DOMContentLoaded', ()=>{
  const btn = document.getElementById('loginBtn');
  if (!btn) return;
  btn.addEventListener('click', ()=>{
    const u = document.getElementById('username').value;
    const p = document.getElementById('password').value;
    const user = new User();
    alert(user.validate(u,p));
  });
});
