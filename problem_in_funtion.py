#write a function fo find maximum of three numbers in python

def maximum(a,b,c):
    if a>b and a>c:
        print("maximum",a)
        return a

    elif b>c and b>a:
        print("maximum",b)
        return b
    else:
        print("maximum",c)
        return c
maximum(2,20,4)


#write a python function to create and print a list where the
#values are square of numbers between 1 and 30.
def create_list():
    l=[]
    for i in range(1,31):
        l.append(i**2)
    return l
print(create_list())
#wap that takes number as a parameter and check if the num is
#prime or not.
print()

def check_prime(n):
    if n==1:
        print("not prime")

    if n==2:
        print("prime")
    if n>2:
        print("not prime")

    for i in range(2,n):
        if n%i==0:
            print("not prime")
            break

    else:
            print("it is a prime")


check_prime(10)

#wa python funcn to sum all the numbers in a list.
def add(numbers):
    answer=1
    total=0
    for i in numbers:
        total=total+i
    return total
print(add([1,2,3,4,5]))

#write a python program to solve the fibonacci sequence using
#recursion
print()

def fs(num):
    if num==1:
        return 0
    elif num==2:
        return 1
    else:
        return fs(num-1)+fs(num-2)
print(fs(7))
