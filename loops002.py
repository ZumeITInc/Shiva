for num in range(0,11,2):
    print(num)
a=list(range(2,11,2))
print(a)
index=0
word='shiva'
for letter in word:
    print((index,letter))
    index=index+1
for item in enumerate(word):
    print(item)
l1=[1,2,3]
l2=['a','b','c']
for items in zip(l1,l2):
    print(items)
