import math
"Data Types and examples of types in action"

# String
'Python'
'Hello'

# Booleans
True
False

# List (ordered collection which allows you to store different data types)
[0, 10, False, True, "This is cool"]

# Dictionary
{
    'first name':'Aveinn',
    'last name':'Swar',
    'country':'USA',
    'major':'CS',
    'skills':{'swe', 'teamwork', 'hardworking'}
}

# Tuple (same as list but cannot be modified once created)
('Aveinn', 'Cool', 'Cannot', 'Change', 'Anymore')

# Set(same as tuple and list but not an ordered collection and stores only unique items)
{'no', 'dupes', 'not ordered'}

# Checking data types
checkType1 = type(10)
checkType2 = type({'hello', 'hi', 'bye'})
checkType3 = type("Hello")
checkType4 = type({'first name': "hello", 
                   "money":12})

print(checkType1)
print(checkType2)
print(checkType3)
print(checkType4)

# Some sample code

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Aveinn'))  # String
print(type([1, 2, 3]))   # List
print(type({'first name':'Aveinn'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple


# Exercise: Level 3
# Calculating Euclidian distance between (2, 3) and (10, 8)

d = ((10 - 2)**2) + ((8-3)**2) 
print(math.sqrt(d))


