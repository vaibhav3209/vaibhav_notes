document.addEventListener("DOMContentLoaded", function () {
  const body = document.body;

  const btn = document.createElement("button");
  btn.id = "notebook-toggle";
  btn.title = "Toggle notebook view";
  btn.innerHTML = "📓";
  body.appendChild(btn);

  function buildNotebookPages() {
    const container = document.querySelector('.md-content__inner');
    if (!container || container.dataset.paginated === 'true') return;

    const markers = Array.from(container.querySelectorAll('.page-marker'));
    if (markers.length === 0) return;

    const children = Array.from(container.children);
    const pages = [];
    let current = document.createElement('div');
    current.className = 'notebook-page';

    children.forEach((child) => {
      if (child.classList.contains('page-marker')) {
        if (current.children.length > 0) pages.push(current);
        current = document.createElement('div');
        current.className = 'notebook-page';
        child.remove();
      } else {
        current.appendChild(child);
      }
    });
    if (current.children.length > 0) pages.push(current);

    pages.forEach((page, i) => {
      if (i === 0) page.classList.add('active');
      container.appendChild(page);
    });

    const pager = document.createElement('div');
    pager.className = 'notebook-pager';
    pager.innerHTML =
      '<button class="pager-prev">← Prev</button>' +
      '<span class="page-count">Page 1 of ' + pages.length + '</span>' +
      '<button class="pager-next">Next →</button>';
    container.appendChild(pager);

    let activeIndex = 0;
    const countLabel = pager.querySelector('.page-count');
    const prevBtn = pager.querySelector('.pager-prev');
    const nextBtn = pager.querySelector('.pager-next');

    function updatePager() {
      pages.forEach((p, i) => p.classList.toggle('active', i === activeIndex));
      countLabel.textContent = 'Page ' + (activeIndex + 1) + ' of ' + pages.length;
      prevBtn.disabled = activeIndex === 0;
      nextBtn.disabled = activeIndex === pages.length - 1;
    }

    prevBtn.addEventListener('click', () => {
      if (activeIndex > 0) { activeIndex--; updatePager(); }
    });
    nextBtn.addEventListener('click', () => {
      if (activeIndex < pages.length - 1) { activeIndex++; updatePager(); }
    });

    updatePager();
    container.dataset.paginated = 'true';
  }



  btn.addEventListener("click", function () {
    body.classList.toggle("notebook-mode");
    const isOn = body.classList.contains("notebook-mode");
    localStorage.setItem("notebook-mode", isOn ? "on" : "off");

    if (isOn) {
      buildNotebookPages();
    } 
  });
});