f = open('teste.txt','w')
f.write('ola mundo')
f.close()

with open('teste.txt') as f:
    print(f.read())
