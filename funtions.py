def hello():     #function defination
    print("hello world")

hello()          #function call

print()


def add():   #funtion defination
    a=10
    b=20
    print(a+b)    #funtion call
add()
print()

#passing arguments and parameters to function

def add(a,b):
    print(a+b)
add(22,20)
print()

#arbitary arguments(we can provide multiple values in the form
#of tuples

def hello(*name):
    print("hello,my name is ",name[1])

hello("badal","hari","hira")





