#for loop
from itertools import repeat

for i in range(1,6,2):
    print(i)

for i in range(1,6):
    print("badal khanal")

#print multipication table using for loop
n=int(input("enter the number   "))
for i in range(1,11):
    print(n,"*",i,"=",n*i)

#while loop

n=0
while n<10:
    print(n)
    n+=1


#while true
while True:
    #print("one day you will be scuesfull")

    #it goes into infinite loop
#to stop while loop we user break

while True:
    num1=int(input("enter the first number"))
    num2=int(input("enter the second number"))
    print(num1,"+",num2,"=",num1+num2)
if repeat=="yes":
    break



