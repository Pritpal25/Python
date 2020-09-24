a = 2
b = 2.0
c = 2+1j

print (type(a), type(b), type(c))

a = 1+2j
print(a, "is complex number?", isinstance(a,complex))
print ("a is of int type int ? ", isinstance(a,int))
print(a.real, a.imag)
# List operations

a = [2, 1, 5, 7, 'apple'] #elements can be on any type
print (a)
print (a[2])
print (a[2:4]) #endExclusive
print (a[2:])
print (a[:2]) # 5 - 2nd element is exclusive here

# lists are mutable
a[2] = 'kaku'
print(a)

#tuples are same as lists, but they are immutable
t = (1, 2, 3, 4)
print (t)
#t[2] = 6 #this generates error

# strings are same as tuples - slicing operator usable, no assignment allowed - immutable

s = 'Hello World!'
print(s)
print(s[6:11])
# s[6] = 'm' - this generates error


