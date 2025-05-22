const stripe_public_key = JSON.parse(document.getElementById('id_stripe_public_key').textContent);
const client_secret = JSON.parse(document.getElementById('id_client_secret').textContent);

const stripe = Stripe(stripe_public_key);
const elements = stripe.elements();

const style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

const card = elements.create('card', { style: style });
card.mount('#card-element');
