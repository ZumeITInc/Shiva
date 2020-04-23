#Sets are unordered collections of unique elements.
#Meaning there can only be one representative of the same object.
set1=set()
print(set1)
set1.add(0)
print(set1)
set1.add(2)
print(set1)
#what if we try to add the same element?
#As we already know that set is unordered collections of unique elements
#so it wont allow duplicates
set1.add(2)
print(set1)
#what if we try to add a list with repeated elements into a set.
l1=[1,1,2,2,2]
s1=set(l1)
print(s1)
#As you can see in the output that repeated items from the list are considered as single item.
