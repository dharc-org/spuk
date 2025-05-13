document.getElementById('entitySearch').addEventListener('input', function () {
  const query = this.value.toLowerCase();
  document.querySelectorAll('.cell.entity').forEach(el => {
    el.style.display = el.textContent.toLowerCase().includes(query) ? '' : 'none';
  });
});