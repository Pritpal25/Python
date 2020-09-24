
# ARITHMETIC OPERATORS - all others behave as java
num = 10//3 # floor division - results into whole number adjusted to the left in the number line
print(num)

num = 10**3 # x raised to the power y
print(num)

# COMPARISON OPERATORS - SAME AS JAVA
# >, <, >=, <=, ==, != - All resutl in True or False

# LOGICAL OPERATORS - and, or, not - same as Java


#BITWISE OPERATORS

x = 10; y = 4 # in binary 1010 and 100 respectively

print('x & y ', x & y)
print(x | y)
print(~x)
print(x^y)
print(x >> 2)
print(x << 2)

x += 5  # Can do like this with all the arithmetic and bitwise operators
print(x)

# IDENTITY OPERATORS

x1 = 2; x2=2
y1 = 'Hello'; y2 = 'Hello'
z1 = [1, 2, 3]; z2 = [1, 2, 3]

print(x1 is x2) # interpreter locates them at same place, these are same objects
print(y1 is y2) # same with strings
print(z1 is not z2) # lists are located seprately, even though they are identical

#MEMBERSHIP OPERATORS - test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).
x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y)
