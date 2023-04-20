import json
# this is the excel data (no keys)
filename = 'sample.json'
# Open the file (standard file open stuff)
with open(filename, 'r', encoding= 'utf-8', newline= '') as f:
    # Load the whole json file into an object named people
    people = json.load(f)

print(type(people))

for p in people:
    print(p['Date Joined'])
    print(type(p))
