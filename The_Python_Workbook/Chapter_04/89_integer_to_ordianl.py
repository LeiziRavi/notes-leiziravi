def integre_to_ordinal(number):
    if number == 1:
        return "first"
    elif number == 2:
        return "second"
    elif number == 3:
        return "third"
    elif number == 4:
        return "fourth"
    elif number == 5:
        return "fifth"
    elif number == 6:
        return "sixth"
    elif number == 7:
        return "seventh"
    elif number == 8:
        return "eigth"
    elif number == 9:
        return "nineth"
    elif number == 10:
        return "tenth"
    elif number == 11:
        return "eleventh"
    elif number == 12:
        return "twelth"
    else:
        return ""

def main():
    for number in range(1,13):
        print(f"{number} : {integre_to_ordinal(number)}")

if __name__ == "__main__":
    main()