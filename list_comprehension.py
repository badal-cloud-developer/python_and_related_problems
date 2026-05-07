l1=[20,23,24,25]
l2=[]

for i in l1:
    l2.append(i)

print(l2)

#this will be simplify using list comprehensin method

l3=[i for i in l1 if i>22]
print(l3)