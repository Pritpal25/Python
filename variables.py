import constant

website = "apple.com"
print website

website = "gap.com"
print website

a, b, c = 2, 1.5, "apple.com"
print a, b, c

a = b = c = "hello"
print a, b, c

print(constant.PI)
print constant.CONSTANT_WITH_UNDERSCORE


# None explained
drink = "DRINK"
food = None

def menu(item):
    if item == "DRINK":
        print (drink)
    else:
        print (food)

menu(drink)
menu(food)


#List, Tuple, Dictionary, Set
fruitsList = ["Apple", "Ball", "Cat"]
fruitsTuple = ("Apple", "Ball", "Cat")
fruitsDict = {"a" : "Apple", "b" :"Ball", "c" : "Cat"}
fruitsSet = {"Apple", "Ball", "Cat", "Apple"}

print(fruitsList)
print(fruitsTuple)
print(fruitsDict)
print(fruitsSet)
