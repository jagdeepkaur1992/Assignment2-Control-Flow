# Task 2: Process multiple orders

from task1 import calculate_discount

def process_orders():
    orders = [1200, 2500, 800, 1750, 3000]

    total_revenue = 0
    discount_count = 0

    print("\n--- ORDER SUMMARY ---")
    print("Amount | Discount | Final Amount")

    for order in orders:
        discount_amount, subtotal, tax, final_total = calculate_discount(order)

        print(f"{order} | {discount_amount} | {final_total}")

        total_revenue += final_total

        # Count orders with discount
        if discount_amount > 0:
            discount_count += 1

    print("\nTotal Revenue:", total_revenue)
    print("Orders with Discount:", discount_count)
