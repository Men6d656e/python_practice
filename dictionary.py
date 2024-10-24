
fruits = {
    "Apple" : 12,
    "orange" : 10,
}

print(fruits)

key = fruits.keys()
valuesoffruits = fruits.values()

print(key)
print(valuesoffruits)

fru = {
    'apple':12,
    'banana':1,
    'peach':2,
    'orange':102,
}
print(fru)

fru["watermellon"] = 300
print(fru)


fru["apple"] = 300
print(fru)

fru1 = {
    'orange':102,
    'apple':102,
}


fru2 = {
    'melon':102,
    'peach':102,
}

fru1.update(fru2)

print(fru1)

fru1.pop("apple")
print(fru1)