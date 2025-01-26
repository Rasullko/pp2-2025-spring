thisset = {"apple", "banana", "apple", False, True, 0,1}
print(thisset)

#access set
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#add set
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#remove set
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

#loop set
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#join set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)
