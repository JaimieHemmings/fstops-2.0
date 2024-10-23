document.addEventListener('DOMContentLoaded', function() {
  let menuToggleBtn = document.getElementById('menu-burger');
  let menu = document.getElementById('nav-overlay');

  menuToggleBtn.addEventListener('click', function() {
    menu.classList.toggle('open');
  });
});