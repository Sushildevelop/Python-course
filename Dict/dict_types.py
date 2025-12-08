# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

dict_student={
    "name":"krish",
    "rollno":25,
    "age":20,
    "school":"xyz"
}
dict_school={
    "name":"xyz",
    "address":"surat gujarat",
    "total_student":5000
}
print("Value of dict student :",dict_student)
print("Data type of dict student :",type(dict_student))

dict_add={**dict_student, **dict_school}
print("Value of dict add :",dict_add)
print("Data type of dict add : ",type(dict_add))













