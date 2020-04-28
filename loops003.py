#what if we try to combine lists of uneven size.
l1=[1,2,3,4,5]
l2=['a','b','c']
for items in zip(l1,l2):
    print(items)
#The output is going to be tuples they are (1,'a'),(2,'b'),(3,'c').
#Here we can see we only get three tuples as we have 5 items in the first list.
#From these we can learn that zip funtion is going to consider the shortest list.
#We can also check is some item in a list or not
l3=[1,2,3]
a='x' in l3
print(a)
#In the output we are going to get false which means the item 'x' is not in the list.
#lets try to check strings.
b='a' in 'shiva'
print(b)
#For integers in a  list to find the maximum or minimum numbers in it we can use 'max' and 'min' function.
l4=[100,250,870,963]
x=min(l4)
print(x)
y=max(l4)
print(y)
