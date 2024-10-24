
s1 = {1,2,3,1,2,3,2}
print(s1)

s1.add(100)
print(s1)

s1.remove(100)
print(s1)

s1.update([12])
print(s1)

set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {2,4,6,8,10,11}

print(set1)
c = set1.union(set2)
d = set1.intersection(set2)
print(c)
print(d)
