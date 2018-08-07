# This file contains basic syntax and brief explanations

# Any single ling comment begins with an octothorpe: '#'
# A multi line comment must have 

# Whitespace: unlock c++ or basic which have semi colons and braces,
# python only uses whitespace for formatting and a fair amount of syntax

# Example:
if True:
    # Everything in this block MUST be indented the same or it will not be considered the same block!
    print("This is inside the if block")
print("This is outside the if block!")
"""
This multiline comment
tells you that
the previous line is not in the "if" statement block!
"""

# Variables
"""
Unlike variables in other languages we've looked at like c++, the python
interpreter doesn't need to be told what kind of variable it is or even
when you're declaring it! This makes things a little trickier for some
things BUT it also makes a few other things a little easier!
"""
# To dimension a string, you just need to list the variable name and assign a value!
name = "bigwavedave"
# To dimension an int or even a float, you just list the name and the value!
age = 26
ageFloat = 26.334
# Man, it's tough getting old.

# This next bit lets us print variables right inside a statement!
# It's like what we saw in js!
exactAge = ageFloat - age
print(f"This is how much older than {age} I really am: {exactAge}")
