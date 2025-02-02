print("Welcome to Mcdonalds please enter the following prices")
kids_meal = float(input("How much does the happy meal for kids cost: "))
adult_meal = float(input("How much does the adult big mac meal cost: "))
kids = int(input("How many kids are there: "))
adult = int(input("how many adults are there: "))
tax = float(input("What is the sales tax rate: "))

print()
print()

tax_rate = float(tax * 0.01)
subtotal = float(kids_meal * kids + adult_meal * adult)
sales_tax = float(subtotal * tax_rate)

print(f"Subtotal: {subtotal:.2f}")


print(f"Sales tax: {sales_tax:.2f}")
ttotal = print(f"Total: {subtotal + sales_tax:.2f}")

pay = float(input("Payment amount: "))
change = float(pay - ttotal)
print(f"Change: {change:.2f}")