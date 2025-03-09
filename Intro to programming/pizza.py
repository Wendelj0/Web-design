# Initialize the shopping cart as an empty list
shopping_cart = []

# Main program loop
while True:
    # Display the menu
    print("\nShopping Cart Menu:")
    print("1. Add item to cart")
    print("2. Display items in cart")
    print("3. Quit")
    
    # Get the user's choice
    choice = input("\nChoose an option (1, 2, or 3): ")
    
    if choice == '1':
        # Add an item to the cart
        item_name = input("Enter the name of the item to add to the cart: ")
        shopping_cart.append(item_name)
        print(f"'{item_name}' has been added to your cart.")
    
    elif choice == '2':
        # Display all items in the cart
        if shopping_cart:
            print("\nItems in your cart:")
            for item in shopping_cart:
                print(f"- {item}")
        else:
            print("\nYour cart is empty.")
    
    elif choice == '3':
        # Exit the program
        print("Thank you for using the shopping cart. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
