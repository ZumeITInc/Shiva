#In function there are two types of arguments
#Which are used to perform tasks in which the arguments has no limit.
#Generally in functions there are arguments which are predefined.
#Lets see a function which add the numbers.
def sum_function(a,b,c,d,e):
    return sum((a,b,c,d,e))
y=sum_function(1,2,3,4,5)
print(y)
#In the above program you can see that only '5' arguments.
#But to do sum of unlimited arguments.
#We can use *args and **kwargs.
#*args is used to add multiple arguments into a function in the form of tupple.
def sum_function(*args):
    return sum(args)
x=sum_function(1,2,3,4,5,6,7,8,9)
print(x)
#As you can see we passed unlimited number of arguments in the above function we got their sum back.
#Here is a program to show how the *args are going to store the items.
def my_function(*args):
    print(args)
my_function(1,2,3,4,5,6)
#In the output you can see that the *args are going to store the arguments in the form of tupple.


