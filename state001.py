#Python statements consists of control flow statements.
#Which can be used to do a task in control manner.
#In order to control this flow of logics we use some keywords.
#To control this flow of logic we use some keywords,They are if,elif,else.
#Control flow syntax makes use of colons and indentation(white space).
#this indentation system is crucial to python and is what sets it apart from other programming languages.
#Syntax of an if statement is given below
#if some_condition:
    #execute some code
#Syntax of an if/else statement
    #if some_condition:
     #execute some code
    #else:
     #do something else
#Syntax of an elif statement
    #if some_condition\
     #execute some code
    #elif some other condition
     #do something different
    #else:
     #do something else
#program to show how an if statement works:
n=1
if n==1:
    print('shiva')
#program to show how an else statement works:
n=1
if n ==1:
    print("the value of n is 1")
else:
    print("the value of n is")
    print(n)
#program to show how an elif statement works:
access_name=input('enter your access_name:')
if access_name=='shiva':
    print('hi shiva access granted')
elif access_name=='zumeit':
    print('hi zumeitans access granted')
else:
    print('no access provided')