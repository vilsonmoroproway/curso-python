set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

#set3 = set1.union(set2)
set3 = set1 | set2
print(set3)

setn = {1, 2, 3, 4}
setn1 = {5, 6, 7 , 8}
setnumeros = setn | setn1
print(setnumeros)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#set3 = set2.difference(set1).union(set1)
set3 = set2.symmetric_difference(set1)
print(set3)