class Student:
    school='AkiraChix'
    def __init__(self,firstname,lastname,age):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age

    def speak(self):
        return f"Hello class,my name is {self.name}"
    def year_of_birth(self):
        return f"Hello {self.name},you were in {2021-self.age}"
    def greet(self):
        return f"Hello {self.firstname} welcome to {self.school}"
    def year_of_birth2(self):
        return f"Hello you were born in {2021-self.age}"
    def initials(self):
        return f"Hello your {self.firstname} {self.lastname}initials are {self.firstname[0]} {self.lastname[0]}"
        



        
    