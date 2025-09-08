// static/js/promo.js
(function () {
    const applyBtn = document.getElementById("apply-promo-btn");
    const clearBtn = document.getElementById("clear-promo-btn");
    const input = document.getElementById("promo-code-input");
    const form = document.getElementById("payment-form");
  
    function getCsrfToken() {
      const el = form && form.querySelector('input[name="csrfmiddlewaretoken"]');
      return el ? el.value : "";
    }
  
    function collectFormData(extra = {}) {
      const data = new URLSearchParams();
      if (form) {
        const fields = form.querySelectorAll("input, select, textarea");
        fields.forEach((el) => {
          if (!el.name) return;
   
          if (el.type === "checkbox" || el.type === "radio") {
            if (el.checked) data.append(el.name, el.value);
          } else {
            data.append(el.name, el.value);
          }
        });
      }
      Object.entries(extra).forEach(([k, v]) => data.set(k, v));
      return data.toString();
    }
  
    async function post(url, bodyStr) {
      await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
          "X-CSRFToken": getCsrfToken(),
        },
        body: bodyStr,
      });
      // Reload to show updated totals and keep form filled
      window.location.reload();
    }
  
    if (applyBtn) {
      applyBtn.addEventListener("click", () => {
        const code = input && input.value ? input.value.trim() : "";
        if (!code) return;
        const url = applyBtn.getAttribute("data-apply-url") || "/checkout/apply-promo/";
        const body = collectFormData({ promo_code: code });
        post(url, body);
      });
    }
  
    if (clearBtn) {
      clearBtn.addEventListener("click", () => {
        const url = clearBtn.getAttribute("data-clear-url") || "/checkout/clear-promo/";
        const body = collectFormData();
        post(url, body);
      });
    }
  })();
  