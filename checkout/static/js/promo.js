// static/js/promo.js

(function () {
    const applyBtn   = document.getElementById('apply-promo-btn');
    const clearBtn   = document.getElementById('clear-promo-btn');
    const input      = document.getElementById('promo-code-input');
  
    const applyForm  = document.getElementById('apply-promo-form');
    const applyCode  = document.getElementById('apply-promo-code');
    const clearForm  = document.getElementById('clear-promo-form');
  
    const paymentForm = document.getElementById('payment-form');
  
    
    const ALLOWED_KEYS = [
      'full_name',
      'email_address',
      'contact_number',
      'address_line_1',
      'address_line_2',
      'town',
      'county',
      'postal_code',
      'country',
    ];
  
    function copyCheckoutFieldsToForm(targetForm) {
      if (!paymentForm || !targetForm) return;
  
      ALLOWED_KEYS.forEach((name) => {
        const src = paymentForm.querySelector(`[name="${name}"]`);
        if (!src) return;
  
        let hidden = targetForm.querySelector(`input[name="${name}"]`);
        if (!hidden) {
          hidden = document.createElement('input');
          hidden.type = 'hidden';
          hidden.name = name;
          targetForm.appendChild(hidden);
        }
        hidden.value = src.value || '';
      });
    }
  
    if (applyBtn && applyForm && applyCode) {
      applyBtn.addEventListener('click', function () {
        applyCode.value = (input?.value || '').trim();
        copyCheckoutFieldsToForm(applyForm);   
        applyForm.submit();                   
      });
  
      input?.addEventListener('keydown', function (e) {
        if (e.key === 'Enter') {
          e.preventDefault();
          applyBtn.click();
        }
      });
    }
  
    if (clearBtn && clearForm) {
      clearBtn.addEventListener('click', function () {
        copyCheckoutFieldsToForm(clearForm);   
        clearForm.submit();
      });
    }
  })();
  