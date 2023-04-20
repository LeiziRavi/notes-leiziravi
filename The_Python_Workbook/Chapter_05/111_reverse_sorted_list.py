def reverse_sort(data):
    reverse_list = sorted(data, reverse = True)
    return reverse_list

def main():
    data = []
    number = int(input("Enter an integer (0 to finish): "))

    while number != 0:
        data.append(number)
        number = int(input("Enter an integer (0 to finish): "))

    reverse_list = reverse_sort(data)
    for i in reverse_list:
        print(i)    

if __name__ == "__main__":
    main()