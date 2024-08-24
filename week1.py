# Favourite Number
favouriteNumber = 11
print(f'My favourite number is {favouriteNumber}')
# String
greeting = 'Hello PLP!'
print(greeting)
# Boolean
isPythonFun = True
isPythonBoring = False
print(f'Is python fun? {isPythonFun}')
print(f'Is python boring? {isPythonBoring}')

# To comment a block of code, use Ctrl + Forward Slash (English Keyboard)

# Control Flow
speed = 80
if speed >= 80:
    print("Fast")
elif speed > 40:
    print("Safe")
else:
    print("Slow")
print("\n")
    
# Loops: For & While
for i in range(8):
    print(f'I Love PLP Academy {i+1}')
    
countdown = 5
while countdown > 0:
    print(f'The Count is: {countdown}')
    countdown -= 1
print("The Count Down is Successful!!!\n")

# Define Function
def greet(person):
    return f"Good Afternoon, {person}"
#Apply the function
print(greet("FrankiZE"))
print(greet("James"))
print(greet("Jane"))
print("\n")

# Lists, Tuples and Dictionaries
# Lists and Tuples
fruitsList = ["Mango", "Cherry", "Orange"]
fruitsTuple = ("Banana", "Apple", "Pineapple")
print(fruitsList)
print(fruitsTuple)

# Dictionaries
Contacts = {
    "Frank": "2643963",
    "Alice": "123456",
    "John": "789012",
    "Mark": "345678"
}
print(f"Frank contact is {Contacts['Frank']}\n")

# Inbuilt Modules
import math
# use a function from module math
result = math.sqrt(49)
print(f'The square root of 49 is  {result}')

# Customized Module
import greet_module
print(greet_module.greet("Jane"))
