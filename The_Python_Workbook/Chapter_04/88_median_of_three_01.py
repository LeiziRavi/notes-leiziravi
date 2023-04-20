def median(a, b, c):
    if a < b and b < c or a > b and b > c:
        return b
    if b < a and a < c or b > a and a > c:
        return a
    if c < a and b < c or c > a and b > c:
        return c


def alternate_median_method(a, b, c):
    return a+b+c - min(a, b, c) - max(a, b, c)


def main():
    a, b, c = map(int, input("Enter three numbers: ").split())
    print(f"Median of {a}, {b}, {c} (by median_method) is {median(a, b, c)}")
    print(
        f"Median of {a}, {b}, {c} (by alternate_median_method) is {alternate_median_method(a, b, c)}")


main()
