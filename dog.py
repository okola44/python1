class Dog:
    legs="four"
    ears="two"
    def __init__(self,breed,name):
        self.breed=breed
        self.name=name
    def bark(self):
        return f"My {self.breed} goes like bark!bark!bark! "
    def sniff(self):
        return f"My {self.name}   can be trained to sniff"


    


