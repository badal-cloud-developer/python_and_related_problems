for i in range(1,6): #rows
    for j in range(1,i+1): #columns
        print(j,end=" ")

    print()

#output
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,6): #rows
    for j in range(1,i+1): #columns
        print("*", end=" ")

    print()
# output
# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1,6): #rows
    for j in range(1,i+1): #columns
        print("i", end=" ")
    print()

