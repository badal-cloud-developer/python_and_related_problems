#unordered collection of data, unique(value is not repeated)
#is called sets and mutable also


a={"ironman","hulk","thor","caption america"}
print(a)


#using loop
for i in a:
    print(i)

#functions of set

#add
a.add("spiderman")
print(a)
#pop
a.pop()
print(a)

print()


#remove
a.remove("hulk")
#discard

#copy

b=a.copy()
print(b)


#more sets functions
z={"ironman","hulk","thor","caption america"}
x={"superman","batman","wonderwoman"}
c={"hulk","thor"}

#isdisjoint

print(z.isdisjoint(c))


#issubset

print(c.issubset(z))

#issuperset
print(z.issuperset(c))


#update
z.update(c)
print(z)

#clear
z.clear()
print(z)



