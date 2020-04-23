#Here come the main difference between the tuple and the list-immutability.
#tuples are immutable.
t1=(1,2,3,4)
print(t1[0])
#if we want to replace the element in index '0' with a string.
t1[0]='new'
print(t1[0])
#it is going to throw a error i.e,'tuple' object does not support item assignment.