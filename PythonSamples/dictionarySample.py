

#dict1 = {'name': 'Harsh', 'age': 14, 'address': 'Luxor Park', 'class': 10}
dict1 = dict(name = 'Harsh', age = 14, address = 'Luxor Park', grade = 10)

print("\nPrint dict using for")
print("------------------------------------")
for key in dict1:
    print(key, dict1[key])

print("\nPrint dict using items()")
print("------------------------------------")
for key, val in dict1.items():
    print(key, " - ", val)

print("\nPrinting all keys")
print("------------------------------------")
for key in dict1.keys():
    print("Keys: ", key)

print("\nPrinting all values")
print("------------------------------------")
for val in dict1.values():
    print("Values: ", val)

print("\nGet one key value using keys")
print("------------------------------------")
print("class: ", dict1.get("grade"))

## update one value using key
print("\nPrint new updated dict")
print("------------------------------------")
dict1["grade"] = 11
print(dict1)
## insert new items in dict at end
dict1["school"] = "Silver Oaks"
print("\nPrint new updated dict")
print("------------------------------------")
print(dict1)

print("\nCreate list from dict")
print("------------------------------------")
list1 = dict1.keys()
list2 = dict1.values()
print(list1)
print(list2)
print("\nPrinting list1 of keys")
print("------------------------------------")
for i in list1:
    print(i)
print("\nPrinting list2 of values")
print("------------------------------------")
for i in list2:
    print(i)

print("Test keys present in dict")
print("------------------------------------")
print('school' in dict1)
print('Fees' in dict1)

print("\nRead keys that is not in dict, thorws Keyerror at runtime")
print("------------------------------------")
try:
    print(dict1["fees"])
except KeyError:
    print("Key doesn't exits")

## use get method to read values if not sure about key, returs None if no key
print("\nRead keys that is not in dict without exception using get()")
print("------------------------------------")
print(dict1.get("fees"))