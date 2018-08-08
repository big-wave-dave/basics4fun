"""
import sys
sys.path.append("../")
"""

# Classes are like our own special data types, like strings and lists.
# Basically, it's a collection of what something is and what something can do.

class Person:
    # These are the properties, or the "things something is":
    name = None
    age = None

    # Come back to this after reading the "define functions" section
    # This is a constructor- it's how to give the properties of the class
    # value when creating an object.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Now we define functions, or the "things something can do"
    # It's just like a normal function, except you need the "self" arg
    # The self arg is a way for the function to know which Person object you're referring to
    def say_name(self):
        print(f"{self.name}")
    def say_age(self):
        print(f"{self.age}")
    
    # Since we're in our class, our functions can act on our properties too!
    def double_age(self):
        self.age *= 2


# Here's how we create objects (variables) of our custom class!
bigwavedave = Person("bigwavedave",26)

# So now we can use our functions on our custom variable!
bigwavedave.say_name()
bigwavedave.say_age()
bigwavedave.double_age()
bigwavedave.say_age()

from otherPersonClass import otherPersonClass
# To use this in another file (just like with libraries from pip!), import it!
# NOTE -- EXTREMELY IMPORTANT: DO NOT USE .py3 FOR MODULES, ONLY .py
# NOTE -- EXTREMELY IMPORTANT: ADD __init__.py TO EACH MODULE'S DIRECTORY
smallwavedave = otherPersonClass("smallwavedave",27,False)

smallwavedave.say_name()
smallwavedave.crySelfToSleep()