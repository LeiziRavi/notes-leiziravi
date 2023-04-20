# formatting wirdth and alignment
"""
< : for left aligned
> : for right aligned
^ : for center aligned
"""

unit_price = 49.95
quantity = 32
sales_tax_rate = 0.065
subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax
output = f"""
Subtotal:  ${subtotal:>9,.2f}
Sales tax: ${sales_tax:>9,.2f}
Total:     ${total:>9,.2f}
"""
print(output)