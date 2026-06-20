fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for x in fruits:
    if 'a' in x:
        newList.append(x)

print(fruits)
print(newList)

newList2 = [x for x in fruits if 'a' in x ]
print(newList2)

newList3 = [x for x in fruits if x != 'apple' ]
print(newList3)

listaMaiscula = [x.upper() for x in fruits]
print(listaMaiscula)
