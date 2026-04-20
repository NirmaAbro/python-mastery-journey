name = input("enter name");
age= int(input("enter your age"));

print("hey your name is:",name,"and your age is",age);

# Arithmetic Operators 
a = 10
b = 3

print(a + b)   # addition
print(a - b)   # subtraction
print(a * b)   # multiplication
print(a / b)   # division
print(a % b)   # modulus (remainder)
print(a ** b)  # power
print(a // b)  # floor division

# 2. Assignment Operators 
x = 5

x += 3   # x = x + 3
x -= 2   # x = x - 2
x *= 4   # x = x * 4


# 3. Comparison Operators 
a = 10
b = 5

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# 4. Logical Operators 
x = 10

print(x > 5 and x < 15)
print(x > 5 or x > 20)
print(not(x > 5))

# Lesson 6: Conditional Statements (if, else, elif) 
age = 18

if age >= 18:
    print("You can vote") 

marks = 75

if marks >= 90:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")


# 4. Nested if (Advanced Basic 🔥) 
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Allowed")
    else:
        print("ID required")
else:
    print("Underage") 

password = "1234"

user_input = input("Enter password: ")

if user_input == password:
    print("Login successful")
else:
    print("Wrong password") 

# Lesson 7: Loops in Python 
# 1. for Loop

# Used when you know how many times to repeat.

for i in range(5):
    print(i)

# 2. range() Variations
# range(start, stop, step)
# Examples:

print(list(range(1, 6)))     # 1 to 5
print(list(range(1, 10, 2))) # odd numbers

# 🔍 Dry Run
# range(1, 6) → 1,2,3,4,5
# range(1,10,2) → 1,3,5,7,9 


# 3. while Loop

# Used when you don’t know how many times to repeat.

i = 0

while i < 5:
    print(i)
    i += 1

# 5. break (Stop Loop)
for i in range(10):
    if i == 5:
        break
    print(i)



# Lesson 8: Functions in Python

# A function is a block of code that runs only when you call it.

# 👉 It helps you:

# Avoid repeating code
# Write clean programs
# Break problems into small parts 

# 1. Basic Function

def greet():
    print("Hello!")

# 2. Function with Parameters

def greet(name):
    print("Hello", name)
greet("Nirma")

# 3. Function with Return Value

def add(a, b):
    return a + b
result = add(5, 3)
print(result)

# 4. Difference: print vs return (VERY IMPORTANT ⚠)

def test():
    print("Hello")

# vs

def test():
    return "Hello"

# 🔍 Difference:
# print	        return
# shows output	gives value back
# cannot store	can store

# 5. Multiple Parameters 

def student(name, age):
    print(name, age)
student("Nirma", 20)

# 6. Default Parameters

def greet(name="Guest"):
    print("Hello", name)
greet()          # Guest
greet("Nirma")   # Nirma


# 7. Real Example

def check_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even(4))

# Lesson 9: Data Structures in Python

# These help you store multiple values in one variable.

# We’ll cover:

# Lists
# Tuples
# Sets
# Dictionaries 


# 🔵 1. List (Most Important 🔥)
# A list stores multiple items (ordered & changeable) 

# 1. List (Most Important 🔥)
# A list stores multiple items (ordered & changeable)

numbers = [1, 2, 3, 4, 5]
names = ["Ali", "Sara", "Nirma"]

# 🔍 Access Elements

print(numbers[0])   # first element
print(numbers[2])

# 🔍 Dry Run
numbers = [1,2,3,4,5]

# index:   0 1 2 3 4 

# numbers[0] → 1
# numbers[2] → 3

# 🔵 Modify List

numbers[0] = 10
print(numbers)

# 🔵 List Methods

numbers.append(6)     # add
numbers.remove(2)     # remove
numbers.pop()         # remove last

# 🔍 Dry Run
# [1,2,3]

# append(6) → [1,2,3,6]
# remove(2) → [1,3,6]
# pop() → [1,3]

# 🔵 Loop Through List
for num in numbers:
    print(num)

# 🟢 Real Example

marks = [80, 70, 90]

total = 0

for m in marks:
    total += m

print(total)


# 🔵 2. Tuple
# Like list but immutable (cannot change)

data = (1, 2, 3)

# ❌ This will give error:

data[0] = 10

# 3. Set
# Unordered
# No duplicates

nums = {1, 2, 2, 3, 4}
print(nums)
# 🔍 Output
# {1,2,3,4} or { 2,1,,5,4,3} the order miht be change in any condition 

# 4. Dictionary (VERY IMPORTANT 🔥🔥)
# Stores data in key-value pairs

student = {
    "name": "Nirma",
    "age": 20,
    "marks": 90
}

# 🔍 Access Data
print(student["name"])

# 🔍 Dry Run 
# student["name"] → "Nirma" 

# 🔵 Modify Dictionary 

student["age"] = 21
student["city"] = "Karachi"

# 🔵 Loop in Dictionary 
for key in student: 
    print(key, student[key])
    
    
# create list of 5 numbers
# print first and last element

count = [1,2,3,4,5];

for j in count:
    print(j);
    
# create list
# add one element
# remove one element


task2 = [1,2,3,4,5];
task2.append(6);
print(task2);
task2.remove(2);
print(task2);

student ={
    "name":"Nirma",
    "age":20,
    "marks":90,
    "city":"Karachi"
}

print("student name is :",student["name"]);
print("student age is :",student["age"]);


number=[];
for i in range(5):
    number.append(int(input("enter number")));
    print (number);
    
print("first number is:",number[0]);
print("last number is:",number[len(number)-1]);



