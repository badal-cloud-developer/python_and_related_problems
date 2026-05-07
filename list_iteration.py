#iteration using for loop
a=["hulk","thor","ironman","caption america"]
for i in a:
    print(i)


#iteration using for loop with range and length function
for i in range(len(a)):
    print(a[i])

#iteration using while loop
i=0
while i<len(a):
    print(a[i])
    i=i+1


#iteration using short-hand for loop
[print(i) for i in a ]