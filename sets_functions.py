

a={"ironman","hulk","thor","caption america"}
b={"superman","batman","wonderwoman"}
c={"hulk","thor","spiderman"}

#union

print(a.union(c))

#difference
print(a.difference(c))


# difference update
print()
a.difference_update(c)
print(a)
# intersection
print()
e=(a.intersection(c))
print(e)
# intersection update
a.intersection_update(c)
print(a)
# symmetric difference

x=a.symmetric_difference(c)
print(x)

# symmetric difference update
a.symmetric_difference_update(c)

print(a)