# Create a generic dictionary for products name product
from math import prod


product = {
    'name':'',
    'unit_price': 0,
    'taxable': True,
    'in_stock': 0,
    'models': []
}

# Create a dictionary for product SKU # DWC001
DWC001 = dict.fromkeys(product.keys())
DWC001.setdefault('taxable',True)
DWC001.setdefault('models',[])
DWC001.setdefault('reorder_point',100)

# Show what;s in the new dictionary
print("Dictionary after fromkeys() and setdefault()")
print(DWC001)


# Change the taxable field from None to True
print("/nDictionary after fromkeys() and setDefault()")
DWC001['taxable'] = True

# Print the dictionary after changing taxable to true
print(DWC001)