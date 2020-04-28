s1='print the words which starts with s in this sentence'
for word in s1.split():
    if word[0] =='w':
        l=[word]
        print(l)
l1=[word for word in s1.split() if word[0]=='w']
print(l1)