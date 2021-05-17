class Car:
    mileage=12000
    tyres=4
    def __init__(self,model,insurance):
        self.model=model
        self.insurance=insurance
    def speed(self):
        return f"my dream car is a red {self.model}"
    def break_down(self):
        return f"the black {self.model} broke down but they had a {self.insurance} insurance"

