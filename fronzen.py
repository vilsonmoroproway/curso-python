x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
x.add('pineaple') #  no work
print(x)

y = {"apple", "banana", "cherry"}
print(type(y))
y.add('orange')
print(y)