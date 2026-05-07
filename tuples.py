#tuple is un-mutable means cannot add or remove after creating it.
a=("apple","banana","mango",1,2,3.4)
print(a)

#single element in tuble is considered string to avoid this put comma
b="apple,"
print(b)

#tuple slicing using index,ie start value,end value,gap
c=("oneplus","twoplus","threeplus")
print(c[1:3])

#conversion of tuples into list and their(using list funcn) functions
W=("oneplus","nokia","redmi")
print("before conversion",type(W))

W=list(W)
print("after conversion",type(W))
W.append("vivo")
print(W)

