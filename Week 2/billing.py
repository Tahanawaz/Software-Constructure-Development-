"""Simple Billing Calculator.

No external libraries imported (pure Python).
Calculates subtotal, discount, tax, and final payable amount.
"""


def calculate_subtotal(items):
    """Calculates subtotal from a list of item prices."""
    return sum(items)


def calculate_discount(subtotal, discount_percent=0.0):
    """Calculates discount amount."""
    return subtotal * (discount_percent / 100)


def calculate_tax(amount_after_discount, tax_percent=0.0):
    """Calculates tax on amount."""
    return amount_after_discount * (tax_percent / 100)


def calculate_final_bill(subtotal, discount, tax):
    """Final total = (subtotal - discount) + tax."""
    return (subtotal - discount) + tax


def display_bill(customer_name, subtotal, discount, tax, total):
    """Prints a clean billing invoice."""
    print("\n==============================")
    print("        INVOICE / BILL        ")
    print("==============================")
    print(f"Customer Name : {customer_name}")
    print("------------------------------")
    print(f"Subtotal      : Rs. {subtotal:.2f}")
    print(f"Discount      : Rs. {discount:.2f}")
    print(f"Tax           : Rs. {tax:.2f}")
    print("------------------------------")
    print(f"Total Payable : Rs. {total:.2f}")
    print("==============================\n")


def main():
    print("=== Simple Store Billing System ===")
    customer_name = input("Enter customer name: ")

    items = []
    item_count = int(input("How many items did the customer purchase? "))

    for i in range(item_count):
        price = float(input(f"Enter price for item {i + 1}: "))
        items.append(price)

    discount_percent = float(input("Enter discount percentage (0 if none): "))
    tax_percent = float(input("Enter tax percentage (0 if none): "))

    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal, discount_percent)
    tax = calculate_tax(subtotal - discount, tax_percent)
    final_total = calculate_final_bill(subtotal, discount, tax)

    display_bill(customer_name, subtotal, discount, tax, final_total)


if __name__ == "__main__":
    main()
