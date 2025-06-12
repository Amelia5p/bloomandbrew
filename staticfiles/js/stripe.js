/* global Stripe */
document.addEventListener('DOMContentLoaded', () => {
  //  Keys from hidden tags
  const stripePublicKey = document
    .getElementById('id_stripe_public_key')
    .textContent.replace(/"/g, '');
  const clientSecret = document
    .getElementById('id_client_secret')
    .textContent.replace(/"/g, '');

  // Initialise Stripe
  const stripe = Stripe(stripePublicKey);
  const elements = stripe.elements();

  // Style card input
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

  // Form
  const form           = document.getElementById('payment-form');
  const errorDiv       = document.getElementById('card-errors');
  const submitButton   = form.querySelector('button');
  const stripePidInput = form.querySelector('input[name="stripe_pid"]');

  // Handle submission
  form.addEventListener('submit', async (evt) => {
    evt.preventDefault();
    submitButton.disabled = true;
    errorDiv.textContent = '';

    // Collect billing name
    const nameField = document.getElementById('id_full_name');
    const billingName = nameField ? nameField.value.trim() : '';

    // Confirm payment
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
      // Show error and re-enable button
      errorDiv.textContent = error.message;
      submitButton.disabled = false;
    } else if (paymentIntent.status === 'succeeded') {
      // On success, attach PID and submit form
      stripePidInput.value = paymentIntent.id;
      form.submit();
    } else {
      errorDiv.textContent = 'Payment could not be processed. Please try again.';
      submitButton.disabled = false;
    }
  });
});
