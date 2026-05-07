#wap to find sum of all the even numbers upto 50.
sum=0
for num in range(1,51):
    if num%2==0:
        sum=sum+num
        print(sum)

#wap to write first 20 numbers and their squared numbers.
for i in range(1,21):
    print(i,i**2)

#wap to find sum of first 10 odd number
#using while loop
# sum=0
# for i in range(1,11):
#     if i%2==0:
#         print("even number")
#     else:
#         sum=sum+i
#         print(sum)

#using while loop
sum=0
n=0
while n<=20:
    if n%2!=0:
        sum=sum+n
    n=n+1
print("the sum of number even number from 1-20 is:",sum)


#wap to check if a number is divisible by 8 and 12 up
#to 100 numbers

for i in range(1,101):
    if i%8==0 and i%12==0:
        print("the number divisible by 8 and 12 is")
        print(i)


#wap to create a billing system at a supermarket
while True:
    name=input("enter customer name:")
    total=0

    while True:
        print("enter the amount and quantity")
        amount=float(input("enter the amount:"))
        quantity=int(input("enter the quantity:"))
        total+=amount*quantity
        repeat=input("do you want to add more items?(yes/no):")
        if repeat=="no":
            break
    print("-"*40)
    print("name:",name)
    print("total amount to be paid:",total)
    print("-" * 40)
    print("*****happy shopping*****")

    repeat1=input("do you want to make bill for next customer?(yes/no):")
    if repeat1=="no":
        break


