"""A small online shop with physical, digital, and payment options."""

from decimal import Decimal


def to_money(amount, description):
    """Convert a value to Decimal and reject invalid or negative amounts."""
    money_amount = Decimal(str(amount))
    if not money_amount.is_finite() or money_amount < 0:
        raise ValueError(f"{description} must be a non-negative amount.")
    return money_amount


class Product:
    """Common product information shared by all product types."""

    product_type = "Product"

    def __init__(self, name, price):
        if not name.strip():
            raise ValueError("Product name cannot be empty.")
        self.name = name
        self.price = to_money(price, "Product price")

    def calculate_total_price(self):
        """Return the product's total cost, including type-specific costs."""
        raise NotImplementedError("Each product type must calculate its cost.")


class PhysicalProduct(Product):
    """A product that has a shipping fee."""

    product_type = "Physical"

    def __init__(self, name, price, shipping_fee):
        super().__init__(name, price)
        self.shipping_fee = to_money(shipping_fee, "Shipping fee")

    def calculate_total_price(self):
        return self.price + self.shipping_fee


class DigitalProduct(Product):
    """A product delivered online, so it has no shipping fee."""

    product_type = "Digital"

    def calculate_total_price(self):
        return self.price


class Order:
    """Keep a customer's products together and calculate their order total."""

    def __init__(self, customer_name):
        if not customer_name.strip():
            raise ValueError("Customer name cannot be empty.")
        self.customer_name = customer_name
        self.items = []

    def add_product(self, product, quantity=1):
        """Add a product and its quantity to the order."""
        if not isinstance(product, Product):
            raise TypeError("Order items must be Product objects.")
        if not isinstance(quantity, int) or quantity < 1:
            raise ValueError("Quantity must be a positive whole number.")

        self.items.append({"product": product, "quantity": quantity})

    def calculate_total(self):
        """Return the total, including each product's own cost rules."""
        return sum(
            (
                item["product"].calculate_total_price() * item["quantity"]
                for item in self.items
            ),
            Decimal("0.00"),
        )

    def display_summary(self):
        """Print each order line and the full total."""
        print(f"Order for {self.customer_name}:")
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            line_total = product.calculate_total_price() * quantity
            print(
                f"  {product.name} ({product.product_type}) x {quantity}: "
                f"${line_total:.2f}"
            )
        print(f"  Order total: ${self.calculate_total():.2f}")


class PaymentMethod:
    """Common payment operation used by all payment methods."""

    def pay(self, amount):
        raise NotImplementedError("Each payment method must implement pay().")


class CardPayment(PaymentMethod):
    """Simulate approving a card payment."""

    def pay(self, amount):
        print(f"Card payment approved: ${amount:.2f}")
        return True


class CashPayment(PaymentMethod):
    """Accept cash when enough has been provided and calculate the change."""

    def __init__(self, cash_received):
        self.cash_received = to_money(cash_received, "Cash received")

    def pay(self, amount):
        if self.cash_received < amount:
            print(
                f"Cash payment declined: received ${self.cash_received:.2f}, "
                f"but the total is ${amount:.2f}."
            )
            return False

        change = self.cash_received - amount
        print(
            f"Cash accepted: ${self.cash_received:.2f}; "
            f"change due: ${change:.2f}"
        )
        return True


class CheckoutService:
    """Connect an order to a selected payment method."""

    def __init__(self, order, payment_method):
        self.order = order
        self.payment_method = payment_method

    def complete_checkout(self):
        """Show the order, request payment, and report the checkout result."""
        self.order.display_summary()
        total = self.order.calculate_total()
        payment_succeeded = self.payment_method.pay(total)

        if payment_succeeded:
            print("Checkout complete.\n")
        else:
            print("Checkout not completed.\n")

        return payment_succeeded


def create_sample_order(customer_name):
    """Build a sample order containing both physical and digital products."""
    order = Order(customer_name)
    order.add_product(PhysicalProduct("Keyboard", "45.00", "5.00"))
    order.add_product(PhysicalProduct("Paperback book", "12.50", "3.00"))
    order.add_product(DigitalProduct("Python e-book", "9.99"), quantity=2)
    return order


if __name__ == "__main__":
    card_order = create_sample_order("Amina")
    card_checkout = CheckoutService(card_order, CardPayment())
    print("--- Card checkout ---")
    card_checkout.complete_checkout()

    cash_order = create_sample_order("Amina")
    cash_checkout = CheckoutService(cash_order, CashPayment("100.00"))
    print("--- Cash checkout ---")
    cash_checkout.complete_checkout()