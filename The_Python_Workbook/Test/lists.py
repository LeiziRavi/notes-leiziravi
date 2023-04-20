data = [2.71, 3.14, 1.41, 1.62]
data.append(2.30)
print(data)
print("=======================================")
data = [2.71, 3.14, 1.41, 1.62]
data.insert(2, 2.30)
print(data)
print("=======================================")
data = [2.71, 3.14, 1.41, 1.62]
data.remove(1.62) # Remove 1.62 from the list
print(data)
last = data.pop() # Remove the last element from the list

print(data)
print(last)