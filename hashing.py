myDict = {
    "name" : "Ram",
    "rollno" : 96,
    "cgpa" : 7.8
}
#access the data
print(myDict["name"])

myDict["cgpa"] = 9.8
print(myDict)

myDict["gender"] = "Male"
print(myDict)

del myDict["gender"]
print(myDict)

print(myDict.keys())

for i in myDict.keys():
    print("key => values")


