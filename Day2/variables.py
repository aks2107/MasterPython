# Variables in Python

# Variable naming rules in Python

"""
1. Must start with a letter or underscore character
2. Cannot start with a number
3. Only contain alpha-numeric characters and underscores (A-z, 0-9, and _)
4. Names are case-sensitive (Variable names that are the same but spelled differently are different variables)
"""


# valid variable names
"""
firstname
lastname
age
country
city
num1
num2
__himiothy__
"""

# invalid variable names

"""
first-name
first@name
num-1
1num
"""

# Python developers use snake_case variable naming convention

"""
Underscore used after each word if a variable contains more than one word.
"""

# Sample variables
first_name = 'Aveinn'
last_name = 'Swar'
country = 'USA'
state = 'NYC'
age = 2000
is_married = False
skills = ['Python', 'SWE', 'Java :(']
person_info = {
   'firstname':'Aveinn',
   'lastname':'Swar',
   'country':'USA',
   'state':'NY'}

# Using built in print and length functions

print('First name:', first_name)
print('Length of first name:', len(first_name))
print('Last name:', last_name)
print('Last name length:', len(last_name))


# Declaring multiple variables in a line

first_name, last_name, age, state = 'Aveinn', 'Swar', 1652, 'NY'
print(first_name, last_name, country, age, state)


# Getting input from the user

first_name = input("What is your first name? ")
age = input("What is your age? ")

print(first_name, age)

# Casting (Converting one data type to another data type)

# int to float

num_int = 10
num_float = float(num_int)

# int to string

num_int = 10
num_str = str(num_int)

# str to int or float

num_str = '10.6'
num_float = float(num_str)
num_int = int(num_float)

#str to list

first_name = 'Aveinn'
name_list = list(first_name)







