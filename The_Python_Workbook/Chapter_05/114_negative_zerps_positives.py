import itertools
number = input("Enter an integer(blank to finish): ")
positives = []
negatives = []
zeroes = []

while number != "":
    number = int(number)
    if number < 0:
        negatives.append(number)
    elif number == 0:
        zeroes.append(number)
    else:
        positives.append(number)

    number = input("Enter an integer(blank to finish): ")

for i in itertools.chain(negatives, zeroes, positives):
    print(i)