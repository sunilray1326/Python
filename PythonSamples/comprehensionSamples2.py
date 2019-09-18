
## comprehension samples

import collections

## find max occurence of a character in a given sentence/string
str1 = "school is boring so ran away simply"
## read character by character and build list except when is it a space ' ' beyween words
list1 = [i for i in str1 if i != ' ']
print("\nList : ", list1)
print("Total characters in list are : ", len(list1))
print("Unique characters in list are: {}".format(len(set(list1))))
maxOccur = max(set(list1), key=list1.count)
print("Max occured char is '{}' and it occured '{}' times".format(maxOccur, list1.count(maxOccur)))

print("Printing counter output")
c = collections.Counter(str1)
del c[' ']
print("\nCounter output  =>  ", c)
print("\nMost common elements are  =>   ", c.most_common(3))
print("--------------------------------------------------------")

## find all index of min and max value in list
list2 = [5, 10, 15, 40, -20, 25, -10, 0, 38, -20, 22, 30, -20, 40]
minval = min(list2)
ind = [i for i, v in enumerate(list2) if v == minval]
print("Min value {} appears at => {} positions in list".format(minval,ind))
maxval = max(list2)
ind = [i for i, v in enumerate(list2) if v == maxval]
print("Max value {} appears at => {} positions in list".format(maxval,ind))

print("\n")