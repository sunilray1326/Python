
## comprehension samples

## find max occurence of a character in a given sentence/string
str1 = "school is boring so ran away simply"
## read character by character and build list except when is it a space ' ' beyween words
list1 = [i for i in str1 if i != ' ']
print("\nList : ", list1)
print("Total characters in list are : ", len(list1))
print("Unique characters in list are: {}".format(len(set(list1))))

## find max occurance of all characters but we can avoid doing it multiple times for same character so use SET
maxOccur = max(set(list1), key=list1.count)
#print(f"Max occured char is '{maxOccur}' and it occured '{list1.count(maxOccur)}' times")
print("Max occured char is '{}' and it occured '{}' times".format(maxOccur, list1.count(maxOccur)))


## Find occurence of each char in list and print
print("\nOccurence of each character in list")
# dict1 = dict()
# for i in set(list1):
#     dict1[i] = list1.count(i)

## we are using dict comprehension to create a dict
dict1 = {i:list1.count(i) for i in set(list1)}
print(dict1)

print("\nPrinting sorted dict values")
print(sorted(dict1.items(), key=lambda t:t[1], reverse = True))
print("--------------------------------------")


# ## Manual navie approach - use 2 list to store key & value and find max 
# ## and, delete max so we can find next max till list exhausted
# print("\nCreating list from dict1 keys and values")
# keyList = list(i for i in dict1.keys())
# valList = list(i for i in dict1.values())
# print("--------------------------------------")
# while len(valList):
#     maxPOS = valList.index(max(valList))
#     print(keyList[maxPOS], valList[maxPOS], end = ', ')
#     del keyList[maxPOS]
#     del valList[maxPOS]    

print("\n")