word = input("Enter a word (blank to finish): ")
words = []
while word != "":
    if words.count(word) == 0:
        words.append(word)
    word = input("Enter a word (blank to finish): ")

for word in words:
    print(word)