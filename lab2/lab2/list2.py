#list comperhension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#sort lists
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#copy lists
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#join lists
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)
