kids_meal = float(input("How much does the kids meal cost: "))
adult_meal = float(input("How much does the adult meal cost: "))
kids = int(input("How many kids are there: "))
adult = int(input("how many adults are there: "))
tax = float(input("What is the sales tax: "))
print()
print()
subtotal = float(kids_meal * kids + adult_meal * adult)
total = float(subtotal + tax)
print(f"Subtotal: {subtotal}")
print(f"Sales tax: {tax}")
print(f"Total: {total}")
print()
pay = float(input("Payment amount: "))
change = float(pay - total)
print(f"Change: {change}")