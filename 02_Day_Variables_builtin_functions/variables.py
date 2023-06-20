#Variables in python
first_name = 'Jorge'
last_name = 'Triana'
country = 'Ecuador'
city = 'Quito'
age = 250

is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname': 'Jorge',
    'lastname': 'Triana',
    'country': 'Ecuador',
    'city': 'Quito',
}

# Printing the values stored in the variables
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)


# Declaring multiple variables in one line
first_name, last_name, country, age, is_married = 'Jorge', 'Triana', 'Ecuador', 38, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

#Getting user input using the input() built-in function.
# first_name = input('What is your name: ')
# age = input('How old are you? ')

# print(first_name)
# print(age)

# Different python data types
# Let's declare variables with various data types

first_name = 'Jorge'     # str
last_name = 'Triana'     # str
country = 'Ecuador'      # str
city= 'Quito'            # str
age = 38                 # int, it is not my real age, don't worry about it

# Printing out types
print(type('Triana'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))     # list
print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set


#Casting: Converting one data type to another data type.
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
# num_int = 10
# print(num_int)                  # 10
# num_str = str(num_int)
# print(num_str)                  # '10'

# str to int or float
# num_str = '10.6'
# print('num_int', int(num_str))      # 10
# print('num_float', float(num_str))  # 10.6

# # str to list
# first_name = 'Asabeneh'
# print(first_name)               # 'Asabeneh'
# first_name_to_list = list(first_name)
# print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']


#Exercises - Day 2
# Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
# Write a python comment saying 'Day 2: 30 Days of python programming'
# Declare a first name variable and assign a value to it
# Declare a last name variable and assign a value to it
# Declare a full name variable and assign a value to it
# Declare a country variable and assign a value to it
# Declare a city variable and assign a value to it
# Declare an age variable and assign a value to it
# Declare a year variable and assign a value to it
# Declare a variable is_married and assign a value to it
# Declare a variable is_true and assign a value to it
# Declare a variable is_light_on and assign a value to it
# Declare multiple variable on one line

#Day 2: 30 Days of python programming
first_name = 'Jorge'
last_name = 'Triana'
full_name = 'Jorge Miguel Triana Gorozabel'
country = 'Ecuador'
city = 'Quito'
age = 38
year = 2023
is_married = False
is_true = True
is_light_on = False
hello, world = 'Hello', 'World'

# Exercises: Level 2
# Check the data type of all your variables using type() built-in function
# Using the len() built-in function, find the length of your first name
# Compare the length of your first name and your last name
    # Declare 5 as num_one and 4 as num_two
    # Add num_one and num_two and assign the value to a variable total
    # Subtract num_two from num_one and assign the value to a variable diff
    # Multiply num_two and num_one and assign the value to a variable product
    # Divide num_one by num_two and assign the value to a variable division
    # Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
    # Calculate num_one to the power of num_two and assign the value to a variable exp
    # Find floor division of num_one by num_two and assign the value to a variable floor_division
# The radius of a circle is 30 meters.
    # Calculate the area of a circle and assign the value to a variable name of area_of_circle
    # Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
    # Take radius as user input and calculate the area.
# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(hello))
print(type(world))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one + num_two
division = num_one + num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30
pi = 3.1416
area_of_circle = (radius * pi) ** 2
circum_of_circle = 2 * pi * radius

radius_input = input ('add radious: ')
area_of_circle = (float(radius_input) * pi) ** 2
print(area_of_circle)

first_name = input('Your firstname')
last_name = input('Your lastname')
country = input('Your country')
age = input('Your age')

print('First name', first_name)
print('Last name', last_name)
print('Country', country)
print('Age', age)
