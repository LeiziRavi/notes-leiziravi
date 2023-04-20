"""
    A particular retailer is having a 60 percent off sale on a variety of discontinued
    products. The retailer would like to help its customers determine the reduced price
    of the merchandise by having a printed discount table on the shelf that shows the
    original prices and the prices after the discount has been applied. Write a program that
    uses a loop to generate this table, showing the original price, the discount amount,
    and the new price for purchases of $4.95, $9.95, $14.95, $19.95 and $24.95. Ensure
    that the discount amounts and the new prices are rounded to 2 decimal places when
    they are displayed.

"""

# Create a array of all the original price
original_price = [4.95, 9.95, 14.95, 19.95, 24.95]

# Loop over each original_price
for i in original_price:
    # for each original_price calculate 60% discount by multiplying the price with 0.6.
    discount_amount = i * 0.6
    # new_price is original_price - discount_amount
    new_price = i - discount_amount
    # Print original_price, formatted discount_amount and formatted new_price
    print("Original price: ", i, "\n",
          "Discount amount: ", format(discount_amount, "0.2f"), "\n",
          "New price: ", format(new_price, "0.2f"))
    print("loop loop")

print("Loop is finsihed.")
