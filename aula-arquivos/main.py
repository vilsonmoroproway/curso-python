f = open('demo.txt')
print(f.read())
f.close()

f = open('demo.txt')
print(f.read(6))
f.close()

with open("demo.txt") as f:
  print(f.read(5))

f = open('demo.txt')
print(f.readline())
f.close()

with open("demo.txt") as f:
  print(f.readline())

