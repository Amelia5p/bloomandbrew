document.addEventListener('DOMContentLoaded', function() {
	const toggleBtn = document.getElementById('search-toggle');
	const searchForm = document.getElementById('search-form');

	if (toggleBtn && searchForm) {
		// Toggle search form when icon is clicked
		toggleBtn.addEventListener('click', function(e) {
			e.stopPropagation();
			searchForm.classList.toggle('show');
		});

		// Hide the search form when clicking outside
		document.addEventListener('click', function(e) {
			const isClickInside = searchForm.contains(e.target) || toggleBtn.contains(e.target);
			if (!isClickInside) {
				searchForm.classList.remove('show');
			}
		});

		// Back to top button
		const backToTopBtn = document.getElementById("backToTopBtn");

		if (backToTopBtn) {
			window.addEventListener("scroll", function() {
				const shouldShow = window.scrollY > 300;
				backToTopBtn.style.display = shouldShow ? "block" : "none";
			});

			backToTopBtn.addEventListener("click", function(e) {
				e.preventDefault();
				window.scrollTo({
					top: 0,
					behavior: "smooth"
				});
			});
		}
	}
});