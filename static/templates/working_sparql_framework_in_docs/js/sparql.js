document.getElementById('exampleSelect').addEventListener('change', function() {
  if (this.value) document.getElementById('query').value = this.value;
});
document.getElementById('run').addEventListener('click', async () => {
  const ep = document.getElementById('endpoint').value;
  const q  = document.getElementById('query').value;
  const url = ep + '?query=' + encodeURIComponent(q);
  const headers = { 'Accept': 'application/sparql-results+json' };
  const resultsDiv = document.getElementById('results');
  try {
    const res = await fetch(url, { headers });
    if (!res.ok) throw new Error(res.status + ' ' + res.statusText);
    const json = await res.json();
    const vars = json.head.vars;
    let html = '<table class="table table-striped"><thead><tr>';
    vars.forEach(v => { html += `<th>${v}</th>`; });
    html += '</tr></thead><tbody>';
    json.results.bindings.forEach(row => {
      html += '<tr>';
      vars.forEach(v => { html += `<td>${row[v]?.value || ''}</td>`; });
      html += '</tr>';
    });
    html += '</tbody></table>';
    resultsDiv.innerHTML = html;
  } catch (err) {
    resultsDiv.innerHTML = `<div class="alert alert-danger">Error: ${err.message}</div>`;
  }
});