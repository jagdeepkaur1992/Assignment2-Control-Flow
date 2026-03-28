# Task 1: Discount Calculator

def calculate_discount(order_amount):
    # Apply discount rules
    if order_amount >= 2000:
        discount = 0.15
    elif 1500 <= order_amount < 2000:
        discount = 0.10
    elif 1000 <= order_amount < 1500:
        discount = 0.07
    else:
        discount = 0.0

    # Calculate discount amount
    discount_amount = order_amount * discount
    subtotal = order_amount - discount_amount

    # Add 5% tax (optional)
    tax = subtotal * 0.05
    final_total = subtotal + tax

    return discount_amount, subtotal, tax, final_total


def run_task1():
    try:
        # Take user input
        order_amount = float(input("Enter order amount: "))

        discount_amount, subtotal, tax, final_total = calculate_discount(order_amount)

        print("\n--- BILL DETAILS ---")
        print("Original Amount:", order_amount)
        print("Discount:", discount_amount)
        print("Subtotal:", subtotal)
        print("Tax (5%):", tax)
        print("Final Total:", final_total)

    except ValueError:
        print("❌ Invalid input! Please enter a numeric value.")