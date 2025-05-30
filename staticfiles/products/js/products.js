document.addEventListener('DOMContentLoaded', function () {
    const categorySelect = document.getElementById('category');
    if (categorySelect) {
      categorySelect.addEventListener('change', function () {
        this.form.submit();
      });
    }
  });

  // Customer review star rating

  document.addEventListener('DOMContentLoaded', function () {
    const stars = document.querySelectorAll('.star-rating i');
    const ratingInput = document.querySelector('input[name="rating"]');

    stars.forEach((star) => {
        star.addEventListener('mouseenter', () => {
            const val = parseInt(star.dataset.value);
            stars.forEach(s => {
                s.classList.toggle('hovered', parseInt(s.dataset.value) <= val);
            });
        });

        star.addEventListener('mouseleave', () => {
            stars.forEach(s => s.classList.remove('hovered'));
        });

        star.addEventListener('click', () => {
            const selectedVal = parseInt(star.dataset.value);
            ratingInput.value = selectedVal;
            stars.forEach(s => {
                s.classList.toggle('selected', parseInt(s.dataset.value) <= selectedVal);
            });
        });
    });
});

  