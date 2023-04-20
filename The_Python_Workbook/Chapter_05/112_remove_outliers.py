import sorted_list
import reverse_order

def remove_outliers(data, n):
        sort_list = sorted_list.sort(data)
        for i in range(n):
            sort_list.remove(sort_list[0])
  
        reverse_list = reverse_order.reverse_sort(sort_list)
        for i in range(n):
            reverse_list.remove(reverse_list[0])
        return reverse_list

def main():
    data = [5, 4, 66, -6, 27, 36, 96,78]
    data_copy = data.copy()
    if(len(data) >= 4):
        print("List with removed outliers: ", remove_outliers(data,2))
        print("Original list: ", data_copy)
    else:
        print("Enter valid data, length of list must be greater than n")

main()