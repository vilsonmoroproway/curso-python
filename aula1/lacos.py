print("laços")

x = 1
while x < 10:
    print(x)
    #x = x + 1
    x += 1

print("")

x = 1
while x < 10:
    print(x)
    if x == 5:
        break
    x += 1

print("")
x = 1
while x < 10:    
    if x == 5:
        x += 1
        continue

    print(x)    
    x += 1

print("")
fruits = ["apple", "banana", "cherry","lemon"]
for x in fruits:
  print(x)


print("")
for x in range(1,32, 5):
  print(x)