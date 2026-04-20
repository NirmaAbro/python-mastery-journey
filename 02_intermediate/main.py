class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age


s1 = Person("Nirma" , 20)
print(s1.name)
print(s1.age)




class Rectangle:
    def __init__(self , w , h):
        self.w=w
        self.h=h
        
    def area(self):
        return self.w * self.h
    
o1= Rectangle(2,3)
print("area:", o1.area())