list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

for x in list1:
  list2.append(x)

print(list2)

list1.extend(list2)
print(list1)

print(list1.count('b'))
print(list1.index('b'))
list1.pop(1)
print(list1)
