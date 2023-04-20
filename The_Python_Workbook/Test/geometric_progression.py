# Compute the sum of the first n terms of a geometric sequence.
# @param a the first term in the sequence
# @param r the common ratio for the sequence
# @param n the number of terms to include in the sum
# @return the sum of the first n term of the sequence

def sumGeometric(a, r, n):
    # Compute and return the sum when the common ratio is 1
    if r == 1:
        return a*n

    # Compute and return the sum when the common ratio is not 1
    s = a * (1-r**n)/(1-r)

    return s


def main():
    # Read the initial value for the first sequence
    init = float(input("Enter the value of a (0 to quit): "))

    while init != 0:
        # Read the ratio and number of terms
        ratio = float(input("Enter the ratio, r: "))
        num = int(input("Enter the number of terms, n: "))

        # Compute and display the total
        total = sumGeometric(init, ratio, num)
        print("the sum of the first", num, "terms is", total)

        # Read the initial value for the next sequence
        init = float(input("Enter the value of a (0 to quit): "))


# Call the main function
main()
