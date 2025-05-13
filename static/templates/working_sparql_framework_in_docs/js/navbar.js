document.addEventListener('DOMContentLoaded', () => {
  const burgers = Array.from(document.querySelectorAll('.navbar-burger'));
  burgers.forEach(burger => {
    burger.addEventListener('click', () => {
      const targetId = burger.dataset.target;
      const menu = document.getElementById(targetId);
      burger.classList.toggle('is-active');
      menu.classList.toggle('is-active');
    });
  });
});