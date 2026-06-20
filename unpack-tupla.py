fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)



(a,*w) = fruits
print(w)

print(len(fruits))
for i in range(len(fruits)):
  print(fruits[i])

print('')
for x in fruits:
    print(x)