
item_names = []
item_prices = []

# shopping cart screen
while True:
    print("shopping cart menu:")
    print("1. Add Item")
    print("2. View items in your cart")
    print("3. View total amount")
    print("4. Remove item")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    # Adding an item to cart
    if choice == '1':
        name = input("Enter the name of the item: ")
        price_input = input("Enter the price of the item: $")
        
        # number checker
        if price_input.replace('.', '', 1).isdigit() and price_input.count('.') <= 1:
            price = float(price_input)
            item_names.append(name)
            item_prices.append(price)
            print(f"Item '{name}' added with a price of ${price:.2f}")
        else:
            print("Please enter a valid number.")

    # view the cart
    elif choice == '2':
        if len(item_names) == 0:
            print("The cart is empty.")
        else:
            print("Your shopping cart:")
            for i in range(len(item_names)):
                print(f"{i + 1}. {item_names[i]} - ${item_prices[i]:.2f}")
                
    # Cart total
    elif choice == '3':
        total = sum(item_prices)
        print(f"Total amount: ${total:.2f}")
        
    # Remove item from cart
    elif choice == '4':
        if len(item_names) == 0:
            print("The shopping cart is empty")
        else:
            item_number = input("Enter the number of the item you want to remove: ")
            
            # number checker
            if item_number.isdigit():
                item_number = int(item_number)
            
                index = item_number - 1
                if 0 <= index < len(item_names):
                    removed_name = item_names.pop(index)
                    removed_price = item_prices.pop(index)
                    print(f"Removed '{removed_name}' with a price of ${removed_price:.2f}")
                else:
                    print("Invalid item number. Please enter a number between 1 and", len(item_names))
            else:
                print("Invalid input. Please enter a number.")

    # Exit the program
    elif choice == '5':
        print("Thank you for using the shopping cart")
        break
    
    # for invalid choices
    else:
        print("Invalid choice. Please select a valid option.")
