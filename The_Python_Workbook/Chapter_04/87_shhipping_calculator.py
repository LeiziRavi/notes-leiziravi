def shippingCalc(no_of_items):
    shipping_charge = 0
    if(no_of_items == 1):
        shipping_charge = 10.95
    else:
        shipping_charge = 10.95 + (no_of_items-1)*2.95
    return shipping_charge


def main():
    no_of_items = int(input("Enter number of items to ship: "))

    print(
        f"Total shipping cost for shipping {no_of_items} = $ {shippingCalc(no_of_items)}")


main()
