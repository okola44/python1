x=[100,110,120,130,140,150]
z=[a*5 for a in x]
print(z)
def divisible_by_three(n):
    for i in range(n):
        if i%3==0:
            print(i)

divisible_by_three(10)


def nested_list():
    x=[[1,2],[3,4],[5,6]]
    
    print(x)

nested_list()


    



    
    
def no_duplicate():
    x = ['a','b','a','e','d','b','c','e','f','g','h']
    y=set(x)
    print(type(y))
    print(y)

no_duplicate()


def divisible_by_seven():
    p=[]
    z=range(100,200)
    for i in z:
        if i%7==0:
            p.append(i)
            print(p)
            

divisible_by_seven()



students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}]
print(type(students))
for student in students:
    name=student["name"]
    age=student["age"]
    print(f"Hello {name} you were born in the year {2021-age}")

class Rectangle:
    def __init__(self,width,length) :
        self.width=width
        self.length=length

    def area(self):
        print( self.width*self.length)

    def perimeter(self):
        print(2*(self.length+self.width))

rectangle1=Rectangle(10,10)
rectangle1.area()
rectangle1.perimeter()





        

        


    
    

