import numpy as np

arr = np.array([1,2,3,4,5])


# print(arr)
# print(type(arr))

n3 = np.zeros((2,3))
n4 = np.zeros((6 , 6))
print(n3)
print(n4)

n5 = np.full((1 , 1) , (10))
print(n5)

n6 = np.arange(10 ,20)
print(n6)


n7 = np.arange(10 ,20 , 2)
print(n7)


n8 = np.random.randint(1,9 , 5)
print(n8)



# multidimentional numpay array
mldrar = np.array([[1,2,3],[1,2,3]])
# mldrar.shape
print(mldrar.shape)
print("------------------------------")
mldrar.shape = (3,2)
print(mldrar.shape)
print(mldrar)

