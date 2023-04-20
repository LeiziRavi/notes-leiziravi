# with open('some_text_file.txt') as f:
#     # Read in entire file
#     content = f.read()
#     print(content)

'''
I've had a perfectly wonderful evening, but this wasn't it.
Grucho Marx
The difference between stupidity and genius is that genius has its limits.
Albert Einstein
We are all here on earth to help others; waht on earth the others are here for, I have no idea.
W. H. Auden
Ending a sentence with a preposition is something up with I will not put.
Winston Churchill
'''

# with open('some_text_file.txt') as f:
#     content = f.readlines()
#     print(content)

'''
["I've had a perfectly wonderful evening, but this wasn't it.\n", 'Grucho 
Marx\n', 'The difference between stupidity and genius is that genius has its 
limits.\n', 'Albert Einstein\n', 'We are all here on earth to help others; 
waht on earth the others are here for, I have no idea.\n', 'W. H. Auden\n', 
'Ending a sentence with a preposition is something up with I will not put.\n', 
'Winston Churchill']

'''


# with open('some_text_file.txt') as f:
#     # Read  in all lines first, then loops through
#     for one_line in f.readlines():
#         print(one_line, end='')

with open('some_text_file.txt') as f:
    # Read  in all lines first, then loops through
    # Count each line starting at zero.
    for one_line in enumerate(f.readlines()):
        # If counter is even number, print with no extra newline
        if one_line[0] % 2 == 0:
            print(one_line[1], end='')
        #Otherwise print a couple spaces and an extra newline
        else:
            print(' ' + one_line[1])

print()

'''
I've had a perfectly wonderful evening, but this wasn't it.
 Grucho Marx

The difference between stupidity and genius is that genius has its limits.
 Albert Einstein

We are all here on earth to help others; waht on earth the others are here for, 
 I have no idea.

W. H. Auden
 Ending a sentence with a preposition is something up with I will not put.

Winston Churchill
'''
