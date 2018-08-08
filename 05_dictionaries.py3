# A dictionary is similar to a list, except instead of JUST an index,
# a dictionary stores two pieces of data: key and value. 
# If I wanted to make a dictionary with names and ages, here's what it would look like:
# Just like a list:
my_dict = {}
my_dict["bigwavedave"] = 26

# Now let's add a second entry.
my_dict["bigwavedad"] = 54

# Now a third and fourth
my_dict["bigwavemom"] = 56
my_dict["bigwaveaunt"] = 56

# What if I want to edit those values to subtract 2 years? It's just like adding them!
my_dict["bigwavedad"] = 52
my_dict["bigwavemom"] = 54

# How do we iterate? Like a list? Well, kind of. We use our for loop again:
for key,value in my_dict.items():
    print(f"{key}:{value}")

# We delete values the same way as with lists with an additional function!
del(my_dict["bigwaveaunt"])

for key,value in my_dict.items():
    if value >= 0:
        print(f"{key}:{value}")