import numpy as np

# vstack()
# hstack()
# column_stack()

n1 = np.array([1,2,3])
n2 = np.array([4,5,6])

vertical = np.vstack((n1,n2))
horizontal = np.hstack((n1,n2))
clmn = np.column_stack((n1,n2))
print(vertical , "vertical ")
print(horizontal , "horizontal")
print(clmn , "clmn")


inter = np.intersect1d(n1,n2)
print(inter)
diff = np.setdiff1d(n1,n2)
print(diff)
diff = np.setdiff1d(n2,n1)
print(diff)

sum = np.sum([n1,n2])
print(sum)

sumindex0 = np.sum([n1,n2],axis=0)
print("sumindex0")
print(sumindex0)


sumindex1 = np.sum([n1,n2],axis=1)
print("sumindex1")
print(sumindex1)

print("aby")
aby = np.array([10,20,30,40,50])
add = aby + 1
sub = aby-1
mul = aby*2
div = aby/2
print(add)
print(sub)
print(mul)
print(div)


# mean median standard devision
print("main median standard devision")

niu = np.array([10,20,30,40,50,60,70,80,90,100])
print("mean")
print(np.mean(niu))
print("median")
print(np.median(niu))
print("std")
print(np.std(niu))


# numpy save lode
print("numpy save and load")
nhu = np.array([1,2,3,4,5,6,7,8,9,10])
np.save('my_array_pynup' , nhu)

nhu2 = np.load("my_array_pynup.npy")
print(nhu2)