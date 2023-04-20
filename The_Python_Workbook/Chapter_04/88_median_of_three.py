from array import array


def median_of_three_numbers(a, b, c):
    return sorted([a, b, c])[1]


def main():
    a, b, c = map(int, input("Enter three numbers: ").split())
    print(f"Median of {a}, {b}, {c} is {median_of_three_numbers(a, b, c)}")


main()
