letter = input("Enter any alphabet: ")

if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
    print(f"{letter} is vowel.")
elif letter in ['y', 'Y']:
    print(f"{letter} is sometimes vowel, sometimes consonant.")
else:
    print(f"{letter} is a consonant.")
