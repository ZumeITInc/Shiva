#Define a function which returns the resistance by taking voltage and current.
def resistance(voltage,current):
    resistance=voltage/current
    return resistance
R=resistance(12,2)
print(R)
#Here you can see the value of resistance from given voltage and resistance.
#In the above function we use return keyword so that to get the result we must assign the return value to a variable.
#Consider there is a function which is used to print the hello.
def sentence_function():
    print('here a sentence is printed')
#Above loc is a function used to print a sentence.
#When we cal the name of the function,it is going to print the statement given in print statement.
sentence_function()


