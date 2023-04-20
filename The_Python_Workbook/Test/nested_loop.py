# Read the first message from the user
message = input("Enter a message(blank to quit): ")

# Loop until the message is a blank line
while message != "":
    # Read the number of times the message should be displayed
    n = int(input("How many times should it be repeadted? "))

    # Display the message the number of times requested
    for i in range(n):
        print(message)

    # Read the next message from the user
    message = input("Enter a message(blank to quit): ")
