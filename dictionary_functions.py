Student={
    "name":"john",
    "class":22,
    "department":"Software Engineer",
    "role":"Engineer"
}

print(Student)

#item

x=Student.get("name")
print(x)

#get
a=Student.items()
print(a)

#keys
b=Student.keys()
print(b)

#values
c=Student.values()
print(c)
#copy

d=Student.copy()
print(d)