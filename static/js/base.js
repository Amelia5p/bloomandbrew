document.addEventListener('DOMContentLoaded', function () {
    const toggleBtn = document.getElementById('search-toggle');
    const searchForm = document.getElementById('search-form');
  
    if (toggleBtn && searchForm) {
      // Toggle search form when icon is clicked
      toggleBtn.addEventListener('click', function (e) {
        e.stopPropagation(); // Prevent click from bubbling up
        searchForm.classList.toggle('show');
      });
  
      // Hide the search form when clicking outside
      document.addEventListener('click', function (e) {
        const isClickInside = searchForm.contains(e.target) || toggleBtn.contains(e.target);
        if (!isClickInside) {
          searchForm.classList.remove('show');
        }
      });
    }
  });
  