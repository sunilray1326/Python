
## comprehension samples

str1 = "school is boring so ran away simply"
## read character by character and build list except when is it a space ' ' beyween words
list1 = [i for i in str1 if i != ' ']
print("\nList : ", list1)
print("Total characters in list are : ", len(list1))
print("Unique characters in list are: {}".format(len(set(list1))))

## find max occurance of a character
maxOccur = max(list1, key=list1.count)
#print(f"Max occured char is '{maxOccur}' and it occured '{list1.count(maxOccur)}' times")
print("Max occured char is '{}' and it occured '{}' times".format(maxOccur, list1.count(maxOccur)))
keySet = set(list1)

print("\nOccurence of each character in list")
dict1 = dict()
for i in set(list1):
    dict1[i] = list1.count(i)
print(dict1)

list2 = dict1.values()
print(list2)
print("\n\n")