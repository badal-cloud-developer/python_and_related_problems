print()
print()
print()

#example

def hello():
    return("Hello World")
print(hello())

#example
def add(a,b):
    return ("the sum is",a+b)
print(add(1,2))

#recursion

# recursion
# def hello():
#     print("Hello World")
#     return hello()
# print(hello())
print()
#find factorial using recursion

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

