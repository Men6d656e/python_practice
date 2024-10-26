num = int(input('Enter a Number: '))
if (num % 2) == 0:
    print(num," even")
else:
    print(num," odd")

# fectorial

number = int(input("Enter The Number"))
fectorial = 1

if number < 0:
    print("Not for Negetive number")
elif number == 0:
    print("the fictorial is 0")
else:
    for x in range(1,number +1):
        fectorial = fectorial * x
    print("The fectorial of ",number," is ",fectorial)
