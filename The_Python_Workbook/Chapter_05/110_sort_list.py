def sort(data):
    sort_list = sorted(data)
    return sort_list

def enter_data():
    data = []
    number = int(input("Enter an integer (0 to finish): "))

    while number != 0:
        data.append(number)

        number = int(input("Enter an integer (0 to finish): "))

    return data

def main():
    data = sort(enter_data())
    
    for i in data:
        print(i)


if __name__ == "__main__":
    main()