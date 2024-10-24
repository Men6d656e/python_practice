

l1 = [ 1,"akash" , 3.14 , True ,3+5j]
type(l1)

print(l1)
print(l1[0])
print(l1[3])
print(l1[1:3])

l1[2] = "saqib"
print(l1)

l1.append(100)
print(l1)

l1.pop()
print(l1)   

# l1.reverse();
# print(l1)
l2 = [3,5,2,7,1,2,3,4,9,0,4,5,6]
l2.sort()
print(l2)

l3 = [5,'akash', 34,2,'k']
print(l3)
# insert ( index , value that w eneed to assign )
l3.insert(2,"mirza")
print(l3)

# concatinate two list
list1 = [1,2,3,4,5,6,6]
list2 = [10,11,12,13,14,15,16,17,18,19,10]
listFinal = list1+list2
listFinal.sort()
print(listFinal)

listTest = [0,2,0]
a = listTest*3
print(a)
