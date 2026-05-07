#here contains keys and value pair

Employee_data = {"name":"badal","age":23,"gender":"male"}
print(Employee_data)
print(Employee_data["name"])
print(Employee_data["age"])

#iteration in dictionary
#using for loop printing key and printing value

print()
print()
print()

for i in Employee_data:
    print(i)
print()
print()
for i in Employee_data:
    print(Employee_data[i])

print()
#using value fucn
for i in Employee_data.values():
    print(i)

#using item funch
print()
for i,j in Employee_data.items():
    print(i,"=",j)


