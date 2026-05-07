#convert the following dictionary into JSON format.
import json
Student_data={
    "name":"david",
    "age":20,
    "marks":100
}
print(type(Student_data))
data=json.dumps(Student_data)
print(data)
print(type(data))

#access the value of age from json data
# data=json.loads(Student_data)
# print(data["age"])

#pretty print followning json data.

data=json.dumps(Student_data,indent=4,separators=(',','='))
print(data)

#sort the following json keys and write them into a file.
f= open("demo.json","w")
json.dump(Student_data,f,indent=4,sort_keys=True)
print("data has been added to the file")