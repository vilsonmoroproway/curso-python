thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print(thisdict["brand"])
print(thisdict.get('model'))

x = thisdict.keys()
print(x)

for i in x:
    print(thisdict.get(i))

for i in x:
    print(thisdict[i])

thisdict['brand'] = 'Toyota'
thisdict.update({'model':'Corolla'})
print(thisdict)

thisdict.update({'color':'vermelha'})
print(thisdict)

thisdict.pop('color')
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict['model']
print(thisdict)

del thisdict
print(thisdict)