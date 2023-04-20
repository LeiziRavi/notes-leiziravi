# Show number in currenct format
currency = lambda n: f"${n:,.2f}"
# Show number in percent format.
percent = lambda n: f"{n:.2%}"

# Test currency function
print(currency(99))
print(currency(123456789.09876543))

# Test percent function
print(percent(0.065))
print(percent(.5))
