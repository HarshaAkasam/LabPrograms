// 1.f add global attributes sample (id, contenteditable already in markup). Add simple validation
document.addEventListener('DOMContentLoaded', ()=>{
  const form = document.getElementById('signupForm');
  if (!form) return;
  form.addEventListener('submit', (e)=>{
    e.preventDefault();
    alert('Sign up form submitted. (Demo)');
  });
});
