window.addEventListener('hashchange', function () {
  const target = document.getElementById(window.location.hash.slice(1));
  const activeDetails = target ? target.closest('details') : null;

  document.querySelectorAll('details[open]').forEach(function (details) {
    if (details !== activeDetails) {
      details.removeAttribute('open');
    }
  });
});