# Task 3: User Menu

orders = []

while True:
    print("\n--- MENU ---")
    print("1 - Add Order")
    print("2 - Show Orders")
    print("q - Quit")

    choice = input("Enter choice: ")

    # Option 1: Add order
    if choice == "1":
        try:
            amount = float(input("Enter order amount: "))
            orders.append(amount)
            print("Order added!")
        except ValueError:
            print("Invalid input!")
            continue   # go back to menu

    # Option 2: Show orders
    elif choice == "2":
        if not orders:
            print("No orders yet!")
            continue

        print("\nOrders List:", orders)
        print("Total Orders:", len(orders))
        print("Total Amount:", sum(orders))

    # Quit
    elif choice == "q":
        print("Exiting program...")
        break

    # Invalid input
    else:
        print("Invalid choice! Try again.")
        continue