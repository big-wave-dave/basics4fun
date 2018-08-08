# Lists! These are arrays from js and c++
# Lists are super easy to make: just like other variables or arrays (ie strings)
myList = []

# Ta da! Empty list. To initialize with values:
myValuableList = [0, 1, 2, 3, 4, "string", 5, '5', "eggs", 3.14]

print(f"{myValuableList[5]} is the 6th element in the list.")

# Now lets change the element!
myValuableList[5] = "sixth"
print(f"{myValuableList[5]} is now the 6th element in the list.")

# What if we wanted to condense that code so we didn't need two print statements?
iter = 0
while iter <= 1:
    print(f"{myValuableList[5]} is the 6th element in the list.")
    myValuableList[5] = "6th"
    iter += 1

# Now let's make the list bigger!
myValuableList.append("theValueToBeAppended!")

# Print everything in the list! This is a preview of for loops for the next one!
for x in myValuableList:
    print(f"{x}")

# Now let's delete a value in the list! We'll delete te 6th element
del(myValuableList[5])

# And now to prove it:
for x in myValuableList:
    print(f"{x}")
# As we can see, "6th" is now gone! All the other elements in the list have
# been moved down by one!