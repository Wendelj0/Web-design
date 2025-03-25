cart = []

while True: #menuscreen

    print("Shopping Cart Menu:")
    print("1. Add item to cart")
    print("2. Display items in cart")
    print("3. Remove item")
    print("4. Calculate cart total")
    print("5. Quit")

        #users choice 
    choice = input("Choose what you would like to do: ") 
            #Adding an item to the cart
    if choice == "1":
        item_name = input("Please enter the itenm you would like to add: ")
        cart.append(item_name)
        print(f"{item_name} were added to your cart")
    elif choice == "2":
        if cart:
            print("Your cart: ")
            for item in cart:
                print(f"* {cart}")
        else:
            print("Your cart is empty")
    
        #next week
    elif choice == "3":
        print("This option is not available please try again next week")
   
        #next week
    elif choice == "4":
        print("This option is not available please try again next week")
   
        #exiting the loop
    elif choice == "5":
        print("Thank you for shopping with us come again soon!")
        break
    
        
        #for invalid choices
    else: 
        print("invalid choice try again")
    
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    # int(input("Welcome to your cart manager\n1. Add an item to cart\n2. View cart\n3. Remove item from cart\n4. Calculate cart total\n5. Quit\nWhat would you like to do: "))
    # if user_choice == 1:
    #     add_item = input("What item would you like to add today? ")
    #     cart.append(add_item)
   
    # elif user_choice == 2:
    #     for i, items in enumerate(cart):
    #         print(f"{i+1}. {cart[i]}")
    # elif user_choice == 3: