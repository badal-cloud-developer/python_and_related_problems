A=["ross","rachel","monica","joe"]

#wap to swap first and fourth element
A[0],A[3]=A[3],A[0]
print(A)

#questions
B=[13,7,12,10]
#find multipicaton of all list numbers of B

mul=1
for i in (B):
    mul*=i

print(mul)

#wap to get largerst number from B
B.sort()
print(B)
print("the largest element is ",B[-1])
print("the largest element is ",max(B))

