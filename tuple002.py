#indexing is also possible in tuple.
#for example
t1=(1,2,3,2)
print(t1[2])
#tuple has feature which can be used to count number of times an element is repeated.
#in the above program the element '2' is repeated twice.
#to know that we can use count() function in tuple.
c1=t1.count(2)
print(c1)
#we can also know the index of particular element in the tuple
#for example if we want to know the index of '3' in the given tuple.
i1=t1.index(3)
print(i1)
#for example if an element is repeated twice.
#it is going to return the index of the element which appeared first.
i2=t1.index(2)
print(i1)