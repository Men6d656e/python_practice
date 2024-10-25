
a = 30;
b = 20;

if a>b :
    print(a,"a ki value")
else:
    print(b,"b ki value")


x=300
y=60
z=70

if (x>y) & (x>z):
    print(x,"x ki value")
elif (y>z) & (y>x):
    print(y,"y ki value")
else:
    print(z,"z ki value")

tup = {1,2,3,4}
if 2 in tup:
    print("we got the six")
else:
    print("can't find  the six")


# if with list

li = [1,2,3,4,5,6]

if li[0]==2:
    li[1]=li[1]+100
    print(li)
else:
    print("ni kiya kam")