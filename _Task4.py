# Task 5: Loop control with conditions

daily = [200, 150, 0, 400, 50, -1, 300]

total_sales = 0

for sale in daily:
    # Stop if corrupted data
    if sale == -1:
        print("Corrupted data found! Stopping...")
        break

    # Skip if no sales
    if sale == 0:
        print("No sales today, skipping...")
        continue

    # Add valid sales
    total_sales += sale
    print("Added:", sale, "| Running Total:", total_sales)

print("\nFinal Total Sales:", total_sales)