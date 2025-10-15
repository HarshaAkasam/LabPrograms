// 4.d DOM: toggle an element's state when link clicked
function toggleCone() {
  const cone = document.getElementById('cone');
  if (!cone) return;
  const isEmpty = cone.dataset.empty === 'true';
  if (isEmpty) {
    cone.textContent = '🍦 (filled)';
    cone.style.background = '#ffe4b5';
    cone.dataset.empty = 'false';
  } else {
    cone.textContent = '🍦 (empty)';
    cone.style.background = '#f0f0f0';
    cone.dataset.empty = 'true';
  }
}
window.toggleCone = toggleCone;
