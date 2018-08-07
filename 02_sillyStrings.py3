# Single Line string:
singleString = "hello"

#multiline strine:
multiString = """first line""" \
    """second line""" \
    """final line"""

#substrings
"""
Substrings are just pieces of strings. Remember when we did js arrays?
That's all a string is! Just an array of characters! So to get a substring,
we just take the starting coordinate and the coordinate one after the end.
"""
fullString = "The Whole String"
subString = fullString[4:9]
print(f"The substring is {subString}")

# Converting numbers (ints and floats) into strings isn't too bad.

# Int:
int1 = 66666
# Float:
float1 = 3.14

# Convert them to strings:
int1_to_string = str(int1)
float1_to_string = str(float1)

# Let's print the converted numbers' substrings!
print(f"Int: {int1_to_string[0:2]} and float: {float1_to_string[0:2]}!")

# Converting from a string to an int/float is easy too:
num_string = '66666'
float_string = '3.14'
to_int = int(num_string)
to_float = float(float_string)

# Now we'll print them added together to prove that they're numbers!
print(f"{num_string} + {float_string} = {to_int+to_float}")
