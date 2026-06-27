import datetime as d

x = d.datetime.now()
print(x)
print(x.strftime('%B'))
print(x.strftime('%b'))

print(f'{x.year} {x.month} {x.day} {x.hour} {x.minute} {x.second}')

print(x.strftime('%V'))
print(x.strftime('%j'))

