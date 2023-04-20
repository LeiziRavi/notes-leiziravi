def reverse_lookup(dictionary, value_to_find):
    keys = []
    for key, value in dictionary.items():
        if value_to_find == value:
            keys.append(key)
    return keys


def main():
    dictionary = {"Science":"subject","History": "subject","Music":"art","Games":"pe"}  
    keys = reverse_lookup(dictionary,"subject")
    if(len(keys)!= 0):
        for key in keys:
            print(key)
    else:
        print("No key found with that particular value.")

if __name__ == "__main__":
    main()