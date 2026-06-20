mytuple = ("apple", "banana", "cherry",'lemon','orange','pineapple')

print(mytuple)
print(mytuple[1])

print(mytuple[-1])
print(mytuple[2:])
print(mytuple[2:5])

print(len(mytuple))

#mytuple.append("pitaya")
mylist = list(mytuple)

print(mytuple)
print(mylist)

mylist.append('strawberry')
print(mylist)

mytuple = tuple(mylist)
print(mytuple)

y = ('cactus',)
print(type(y))

mytuple += y
print(mytuple)