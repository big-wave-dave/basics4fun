# All about control structures, baby!

# If statements:
age = 26
if age >= 18:
    print(f"You're an adult.")
    # Now for else
elif age < 18:
    print(f"Congratulations, you're not an adult. Enjoy yourself!")
else:
    print(f"Wow, no age? I'm impressed. And concerned.")

# Ternary, which is like a 1 line if/else:
oldEnough = True if age >= 18 else False

# While loops are like a way of checking an if statement repeatedly
while age < 65:
    print(f"At age {age}, unfortunately you still have responsibilities before you can retire.")
    age += 1