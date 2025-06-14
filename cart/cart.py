from decimal import Decimal
from products.models import Product


class Cart:
    DELIVERY_THRESHOLD = Decimal('50.00')
    DELIVERY_FEE = Decimal('5.00')

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        current_quantity = self.cart.get(product_id, {}).get('quantity', 0)

        if override_quantity:
            new_quantity = quantity
        else:
            new_quantity = current_quantity + quantity

        if new_quantity > product.stock:
            raise ValueError(
                f"Cannot add {new_quantity} × {product.name}. "
                f"Only {product.stock} in stock."
            )

        self.cart[product_id] = {
            'quantity': new_quantity,
            'price': str(product.display_price()),
        }
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart_copy = self.cart.copy()

        for product in products:
            cart_copy[str(product.id)]['product'] = product

        for item in cart_copy.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(
            Decimal(item['price']) * item['quantity']
            for item in self.cart.values()
        )

    def get_delivery_fee(self):
        total = self.get_total_price()
        return (
            Decimal('0.00')
            if total >= self.DELIVERY_THRESHOLD
            else self.DELIVERY_FEE
        )

    def get_total_due(self):
        return self.get_total_price() + self.get_delivery_fee()

    def clear(self):
        self.session['cart'] = {}
        self.save()
