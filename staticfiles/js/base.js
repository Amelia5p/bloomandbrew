// Hide the search bar in the Nav until clicked
const toggleBtn = document.getElementById('search-toggle');
const searchForm = document.getElementById('search-form');

toggleBtn.addEventListener('click', () => {
  searchForm.classList.toggle('show');
});
