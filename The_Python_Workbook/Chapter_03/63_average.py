"""
    Create a program that computes the average of a collection of values entered by the user. 
    The user will enter 0 as a sentinel value to indicate that no further values will be provided. 
    Your program should display an appropriate error message if the first value entered by the user is 0

"""

# First take anumber from the user
number = int(
    input("Enter an integer to add to the collection(0 to compute the average): "))

# Initialize the sum of numbers at 0
sum = 0
# Initialize the count of numbers entered at 0
count = 0

# While the entered number is 0
if number == 0:
    print("No avg exists.")
else:
    while number != 0:
        # Add the entered number to the sum i.e. sum = sum + number
        sum += number  # sum = sum + number
        # increment the count by 1 for each loop
        count += 1  # count = count + 1
        number = int(
            input("Enter an integer to add to the collection(0 to compute the average): "))

    # Once loop is exited, i.e. 0 is entered, Calculate the average of numbers by dividing the sum with total count of numbers entered.
    average = sum / count
    # Print the average.
    print("Average of entered numbers: ", average)
