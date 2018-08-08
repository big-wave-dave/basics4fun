# Dimension our class
class otherPersonClass:
    # Declare our oPerson's properties (variables!)
    name = None
    age = None
    relationship = None

    # Give us a constructor because we have no default values!
    def __init__(self, name, age, relationship):
        self.name = name
        self.age = age
        self.relationship = relationship
    
    # Now for our methods (functions!)
    def say_name(self):
        print(f"{self.name}")
    def say_age(self):
        print(f"{self.age}")
    def say_relationship(self):
        print(f"{self.relationship}")
    def crySelfToSleep(self):
        if self.relationship is False:
            print(f"Start working out more, loser.")
        else:
            print(f"Maybe this one won't leave you for a while.")
    def double_age(self):
        self.age *= 2
    def haveABirthday(self):
        self.age += 1
