from django.http import HttpResponse
from .models import Order


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle a generic/unknown webhook event."""
        return HttpResponse(
            content=f'Unhandled event type {event["type"]}',
            status=200,
        )

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent.succeeded webhook from Stripe."""
        intent = event.data.object
        pid = intent.id
        metadata = intent.metadata

        try:
            order = Order.objects.get(stripe_pid=pid)
            order.save()
        except Order.DoesNotExist:
            return HttpResponse(
                content=f'Order not found for PID: {pid}',
                status=404,
            )

        return HttpResponse(
            content=f'PaymentIntent {pid} succeeded',
            status=200,
        )

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.payment_failed webhook from Stripe."""
        intent = event.data.object
        return HttpResponse(
            content=f'Payment for {intent.id} failed.',
            status=200,
        )
