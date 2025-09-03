(function () {
    const applyBtn = document.getElementById("apply-promo-btn");
    const clearBtn = document.getElementById("clear-promo-btn");
    const input = document.getElementById("promo-code-input");
  
    function getCsrfToken() {
      const el = document.querySelector(
        '#payment-form input[name="csrfmiddlewaretoken"]'
      );
      return el ? el.value : "";
    }
  
    async function post(url, data) {
      await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
          "X-CSRFToken": getCsrfToken(),
        },
        body: new URLSearchParams(data).toString(),
      });
      // Reload to refresh totals/messages and PI amount
      window.location.reload();
    }
  
    if (applyBtn) {
      applyBtn.addEventListener("click", () => {
        const code = input && input.value ? input.value.trim() : "";
        if (!code) return;
        const url = applyBtn.getAttribute("data-apply-url");
        post(url, { promo_code: code });
      });
    }
  
    if (clearBtn) {
      clearBtn.addEventListener("click", () => {
        const url = clearBtn.getAttribute("data-clear-url");
        post(url, {});
      });
    }
  })();
  