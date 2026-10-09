# Part 1:
def greet_customer():
    print("Welcome to lemonade stand.")
    print("Fresh Lemonade,made just for you.")
    
# Part 2:
greet_customer() 

# Part 3:
price_per_cups = float(input("Enter the price per cup in dollar: "))
cups_sold = int(input("Enter the number of cups sold: "))

# Part 4:
def calculate_total(price,cups):
    total = price * cups
    return total 

# Part 5:
total_cost = calculate_total(price_per_cups,cups_sold)

# Part 6:
rounded_total = round(total_cost,2)
print("Total Cost  :",rounded_total)

# Part 7:
amount_paid = float(input("Enter the amount paid by the customer: "))

# Part 8:
def calculate_change(paid,total):
    change = paid - total
    return change

# Part 9:
change_due = calculate_change(amount_paid,rounded_total)
rounded_change = round(change_due,2)

# Part 10:
def thank_you_message(cups):
    if cups >= 5:
        return "Wow big order! Thanks so much for your support"
    
    else:
        return "Thank you for stopping by the stand"
    
# Part 11:
closing_message = thank_you_message(cups_sold) 

# Part 12:
print("")
print(" ==== LEMONADE STAND RECEIPT ====")
print("Price per cup   :",price_per_cups)
print("Cups sold       :",cups_sold) 
print("Total cost      :",rounded_total)
print("Amount paid     :",amount_paid)
print("Change due      :",change_due) 
print(closing_message)
print("====================================")