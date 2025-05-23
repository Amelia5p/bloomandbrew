/* static/js/stripe.js
 *
 * Handles:
 *  • reading the keys Django injected with {{ …|json_script }}
 *  • mounting the Card Element
 *  • confirming the payment when the form is submitted
 *  • surfacing any Stripe errors to the user
 *  • posting the confirmed PaymentIntent ID back to Django
 */
console.log('[stripe.js] loaded');                      // ➊
document.addEventListener('DOMContentLoaded', () => {
  console.log('[stripe.js] DOMContentLoaded fired');   // ➋

  const stripePublicKey = document
    .getElementById('id_stripe_public_key')
    .textContent.replace(/"/g, '');
  const clientSecret = document
    .getElementById('id_client_secret')
    .textContent.replace(/"/g, '');

  console.log('[stripe.js] keys →', { stripePublicKey, clientSecret }); // ➌
  /* …rest of file… */
});





document.addEventListener('DOMContentLoaded', () => {
    /* ------------------------------------------------------------------
       1.  Grab the public key & client-secret that the template rendered
    ------------------------------------------------------------------ */
    const stripePublicKey = document
      .getElementById('id_stripe_public_key')
      .textContent.replace(/"/g, '');
  
    const clientSecret = document
      .getElementById('id_client_secret')
      .textContent.replace(/"/g, '');
  
    /* ------------------------------------------------------------------
       2.  Initialise Stripe.js and mount the Card Element
    ------------------------------------------------------------------ */
    const stripe = Stripe(stripePublicKey);
  
    const elements = stripe.elements();
    const style = {
      base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': { color: '#aab7c4' }
      },
      invalid: { color: '#dc3545', iconColor: '#dc3545' }
    };
  
    const card = elements.create('card', { style });
    card.mount('#card-element');
  
    /* ------------------------------------------------------------------
       3.  Wire up form submission → stripe.confirmCardPayment()
    ------------------------------------------------------------------ */
    const form          = document.getElementById('payment-form');
    const errorDiv      = document.getElementById('card-errors');
    const submitButton  = form.querySelector('button');
    const stripePidInput = form.querySelector('input[name="stripe_pid"]');
  
    form.addEventListener('submit', async (evt) => {
      evt.preventDefault();
      submitButton.disabled = true;      // prevent double-clicks
      errorDiv.textContent  = '';        // clear prior errors
  
      // Pull whatever billing name field your form uses (adjust selector if needed)
      const billingNameInput = document.getElementById('id_full_name');
      const billingName = billingNameInput ? billingNameInput.value.trim() : '';
  
      const { error, paymentIntent } = await stripe.confirmCardPayment(
        clientSecret,
        {
          payment_method: {
            card,
            billing_details: { name: billingName }
          }
        }
      );
  
      if (error) {
        // Show the error, re-enable the button so user can try again
        errorDiv.textContent = error.message;
        submitButton.disabled = false;
      } else if (paymentIntent.status === 'succeeded') {
        // Stash the confirmed PaymentIntent ID so Django can save it
        stripePidInput.value = paymentIntent.id;
        form.submit();   // hands off to your checkout view
      } else {
        // Unlikely paths: requires_action, etc.
        errorDiv.textContent = 'Payment could not be processed. Please try again.';
        submitButton.disabled = false;
      }
    });
  });
  