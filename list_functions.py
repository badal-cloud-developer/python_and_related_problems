a=["hulk","thor","ironman","caption america"]
print(a)

#length
print(len(a))

#occurance
print(a.count("hulk"))

#add element
a.append("spiderman")
print(a)

#add to specific location
a.insert(2,"vision")
print(a)

#remove element
a.remove("hulk")
print(a)

#remove from a certain location
print(a.pop(1))
print(a)


#more functions of list
b=["thor","ironman","caption america"]

#create copy of list
c=b.copy()
print(c)

#acess an element or to find index
print(b.index("thor"))

#to extend the list
d=["banana","apple","mango"]
b.extend(d)
print(b)

#to reverse the list

b.reverse()
print(b)

#to sort the list
b.sort()
print(b)
#to clear all data from the list
b.clear()
print(b)

