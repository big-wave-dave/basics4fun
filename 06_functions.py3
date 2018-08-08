# Basically, functions DO something.
# You can give it something, it can give you something back, but all it
# has to do is SOMETHING.

# To define a function, you use def nameOfFunction():
def myFirstFunction():
    print(f"This function has no args or anything, but it does SOMETHING.")

def mySecondFunction():
    print(f"This function sends something back!")
    return "send this back"

def myThirdFunction(argument1,argument2):
    print(f"{argument1} is one and {argument2} is two!")
    return argument1,argument2

# To call a function, we just say its name!
print(f"{myFirstFunction()}")
print(f"{mySecondFunction()}")
# Notice in this third function that if I pass in arg string literals, I need to use single quotes in the string format function
print(f"Now for the third function, where we print the multiple returned args: {myThirdFunction('arg1','arg2')}")
# Or use the unpacking syntax for the multiple return values:
returnedVal1, returnedVal2 = myThirdFunction('arg1','arg2')
print(f"Unpacked returned val 1 = {returnedVal1} and unpacked returned val 2 = {returnedVal2}")
