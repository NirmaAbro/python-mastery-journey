# class Person:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age


# s1 = Person("Nirma" , 20)
# print(s1.name)
# print(s1.age)




# class Rectangle:
#     def __init__(self , w , h):
#         self.w=w
#         self.h=h
        
#     def area(self):
#         return self.w * self.h
    
# o1= Rectangle(2,3)
# print("area:", o1.area())


# 1. What is Inheritance?

# Inheritance means:
# One class inherits properties & methods from another class

# class Person:
#     def __init__(self, name):
#         self.name = name 


# class Student(Person):
#     def __init__(self, name, grade):
#         super().__init__(name)   # call parent constructor
#         self.grade = grade

#     def show_grade(self):
#         print("My name is", self.name, "and my grade is", self.grade)


# s1 = Student("Nirma", "A")
# s1.show_grade()

        
# class Animal:
#     def speak(self):
#         print("Animals speaks")
        
# class Dog(Animal):
#     def speak(self):
#         print("Dog Barks")
        
# d1 = Dog()
# d1.speak()

# PART 4: Using super() (Optional but useful)
# What if you want BOTH parent + child?


# Rule:
# Constructor → used to store data
# Methods → used to perform actions

# class Animal:
#     def speak(self):
#         print("Animal sound")

# class Dog(Animal):
#     def speak(self):
#         super().speak()
#         print("Dog barks")
        
# d = Dog()
# d.speak()


# class Account:
#     def __init__(self, balance):
#         self.__balance = balance 
#     def deposit(self, amount):
#         self.__balance += amount
#     def withdraw(self ,amount):
#         self.__balance -= amount
    
#     def get_balance(self):
#         return self.__balance
    
# acc = Account(1000)
# acc.withdraw(500)

# print(acc.get_balance())
        
