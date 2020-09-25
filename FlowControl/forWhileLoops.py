numbers = [2, 4, 6, 8, 10]

sum = 0
for val in numbers:
    sum += val

print (sum)

# RANGE FUNCTION : range(start, endExclusive, step function) - lazy function, doenst generate values when you create it

print(range(10)) # prints 0 to n-1 in python2.7 and range(10) in python3 
print(type(range(10))) # range type in python 3 and list type in python 2
print(list(range(2, 10))) # step function is 1 by default
print(type(list(range(2,10))))
print(list(range(2, 10, 2)))

for i in range(2, 10):
    print(i)

genre = ['pop', 'rock', 'trance']
for i in range(len(genre)):
    print(genre[i])


# FOR ELSE STATEMENT : prints the else part after the for loop is exhausted, 
# if a break is used in for body, else doesnt get executed

for i in range(2, 5):
    print(i)
else:
    print('Numbers exhausted')

# WHILE LOOP IS EXACTLY SAME AS FOR LOOP
# ELSE AND BREAK RULES APPLY THE SAME
# ANY NON ZERO VALUES ARE TRUE
# ZERO AND NONE ARE FALSE
