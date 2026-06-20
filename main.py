mylist = ["apple", "banana", "cherry"]
print(mylist)
print(len(mylist))
print(mylist[1])

mylist[2] = 'lemon'
print(mylist)

mylist.append('orange')
print(mylist)

print('informe uma fruta')
mylist.append(input())
print(mylist)

mylist.remove('banana')
print(mylist)

mylist.pop()
print(mylist)

for x in mylist:
  print(x)