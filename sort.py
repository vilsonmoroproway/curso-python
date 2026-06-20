fruits = ["mango","apple", "banana", "cherry", "kiwi"]
print(fruits)

fruits.sort()
print(fruits)

fruits.sort(reverse = True)
print(fruits)

fruits.reverse()
print(fruits)

fruits[1] = 'Banana'
fruits[3] = 'Kiwi'
fruits.sort(key = str.lower)
print(fruits)