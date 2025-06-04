document.addEventListener('DOMContentLoaded', function () {
  const toggleBtn = document.getElementById('search-toggle');
  const searchForm = document.getElementById('search-form');

  if (toggleBtn && searchForm) {
    let isSearchVisible = false;

    toggleBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      isSearchVisible = !isSearchVisible;
      searchForm.classList.toggle('show', isSearchVisible);
    });

    document.addEventListener('click', function (e) {
      const isClickInside = searchForm.contains(e.target) || toggleBtn.contains(e.target);
      if (!isClickInside) {
        searchForm.classList.remove('show');
        isSearchVisible = false;
      }
    });
  }

  // Back to top button
  const backToTopBtn = document.getElementById("backToTopBtn");

  if (backToTopBtn) {
    window.addEventListener("scroll", function () {
      backToTopBtn.style.display = window.scrollY > 300 ? "block" : "none";
    });

    backToTopBtn.addEventListener("click", function (e) {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }
});
