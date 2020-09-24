# NAME - EVERYTHING IN PYTHON IS AN OBJECT AND HENCE HAS A NAME
a = 2
print(id(a)) # id() gives the memory address of that variable
print(id(2))

a = 3 # a occupies a new address in memory with new value
print(id(a)) 
b = 2 # b now starts pointing to where a was initially
print(id(b)) 


# FUNTIONS ARE OBJECTS TOO, SO THEY CAN BE ASSIGNED TO A NAME AS WELL

def printHello():
    print('Hello')

a = printHello
a() # invoking the method
printHello()


# NAMESPACE - READ ABOUT IT HERE https://www.programiz.com/python-programming/namespace
# every namespace modifies(writes to) the values in their own namespace, unless a particular variable is defined as global.

def outer_function():
    x = 20 # local namespace
    def inner_function():
        x = 30 # local namespace
        print(x)
    inner_function()
    print(x)

x = 10 # global namespace
outer_function()
print (x)




def outer_function():
    global x
    x = 20
    def inner_function():
        global x
        x = 30
        print(x)
    inner_function()
    print(x)

x = 10
outer_function()
print (x)
