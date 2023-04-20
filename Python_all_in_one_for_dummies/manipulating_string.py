s = "Abracadabra Hocus Pocus you're a turtle dove"
# Is there a lowercase letter t is contained in s?
print("t" in s)

# Is there an uppercase letter t is contained in S?
print("T" in s)

# Is there no uppercase T in s?
print("T" not in s)

# Print 15 hyphens in a row
print("-" * 15)

# Print first character in a string s
print(s[0])

# Print characters 33 - 39 from string s
print(s[33:39])

# print every third character in s string at zero
print(s[0:44:3])

# print lowest character in s
print(min(s))

# print the highest character in s
print(max(s))

# where is the first uppercase P?
print(s.index("P"))

# Whwere is the first lowercase o in the latter half of string s
# Note that the returned value still starts counting from zero 
print(s.index("o", 22, 44))

# How many lowercase letters a are in string s?
print(s.count("a"))

print(ord(""))