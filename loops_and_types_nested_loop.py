#nested loop

#a loop inside a loop is called nested loop.it may be for
#loop,while loop,do while loop etc

for i in range(1,4):
    for j in range(1,11):
        print(j,end=" ")

#used to solve pattern problem
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")

    print()

#for loop with condition statement
#wap to find a even number from 1 to 100

for i in range(1,101):
    if i%2==0:
        print("even number")
    else:
        print(i)

#break and continue statement
for i in range(1,10):
    if i==5:
        continue #5 wala number lai escape garxa
    else:
        print(i)


for j in range(1,10):
    if j==7:
        break  #7 aayepaxi loop rokinxa
    else:
        print(j)
print("thank you")






