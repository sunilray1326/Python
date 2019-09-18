

set1 = set([1, 2, 3, 4, 5, 1, 2])
print(set1)

set2 = {3, 4, 5, 3, 4, 6, 7}
print(set2)

print("\nElements that are in set1 but not in set2")
print("---------------------------------------")
print(set1 - set2)
print("\nElements that are in set1 or in set2 - all elements from both sets")
print("---------------------------------------")
print(set1 | set2)
print("\nElements that are either set1 or in set2 - exclusive elememts from each set")
print("---------------------------------------")
print(set1 ^ set2)
print("\nElements that are in set1 and set2 - common elements")
print("---------------------------------------")
print(set1 & set2)

## can create a set from string and it will remove duplicate characters
## set is by default unordered list so every time
print("\nCreating a set from a srting")
set3 = set("I am creating a set from string")
print(set3)
print("Sorted set")
print(sorted(set3))
