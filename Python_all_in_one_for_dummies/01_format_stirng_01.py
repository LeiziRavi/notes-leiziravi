# How to use fString
# Displaying variable inside fStringt
username = "Ravi"
print(f"Hello {username}") # Hello Ravi

# Displaying expression using fString
unit_price = 49.99
quantity = 30
print(f"Subtotal: ${quantity*unit_price}") # Subtotal: $1499.7

# formatting dollar amounts (:,), shows commas in thousand places
print(f"Subtotal: ${quantity*unit_price:,}") # Subtotal: $1,499.7

#format decimal places (.2f) => "two decimal places, fixed"
print(f"Subtotal: ${quantity*unit_price:,.2f}") # Subtotal: $1,499.70

# formatting percent numbers
sales_tax_rate = 0.065
print(f"Sales Tax Rate {sales_tax_rate}") # Sales Tax Rate 0.065
print(f"Sales Tax Rate {sales_tax_rate:.2%}") # Sales Tax Rate 6.50%


# Making multiple format strings
# Method 1
user1 = "Alberto"
user2 = "Babs"
user3 = "Carlos"
output = f"{user1} \n{user2} \n{user3}"
print(output)

# Making multiple format strings
# Method 2
unit_price = 49.95
quantity = 32
sales_tax_rate = 0.065
subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax
output = f"""
Subtotal:  ${subtotal:,.2f}
Sales tax: ${sales_tax:,.2f}
Total:     ${total:,.2f}
"""
print(output)


