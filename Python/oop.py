class Employe:
    def __init__(self, name, age, roll):
        self.name = name
        self.age = age
        self.roll = roll


    def Printdetails(self):
        # print()
        return f"my name is {self.name}, age is {self.age} and roll number is {self.roll}"


e1 = Employe( 'Prashant', 21, 39)
# e1.Printdetails()
print(e1.Printdetails())