const stripe = Stripe(JSON.parse(document.getElementById('id_stripe_public_key').textContent));
const clientSecret = JSON.parse(document.getElementById('id_client_secret').textContent);

const elements = stripe.elements();
const card = elements.create('card');
card.mount('#card-element');

card.on('change', function (event) {
    const errorDiv = document.getElementById('card-errors');
    errorDiv.textContent = event.error ? event.error.message : '';
});
