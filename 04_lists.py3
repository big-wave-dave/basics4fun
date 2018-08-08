# Lists! These are arrays from js and c++
# Lists are super easy to make: just like other variables or arrays (ie strings)
myList = []

# Ta da! Empty list. To initialize with values:
myValuableList = [0, 1, 2, 3, 4, "string", 5, '5', "eggs", 3.14]

print(f"{myValuableList[5]} is the 6th element in the list.")

# Now lets chance the element!
myValuableList[5] = "sixth"
print(f"{myValuableList[5]} is now the 6th element in the list.")

# What if we wanted to condense that code so we didn't need two print statements?
iter = 0
while iter <= 1:
    print(f"{myValuableList[6]} is the 6th element in the list.")
    iter += 1

