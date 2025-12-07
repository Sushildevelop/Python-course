# Tuple data types are used to store multiple items in a single variable 
# why we use tuple? -  tuple items are ordered, unchangeable, and allow duplicate values

tuple_value=(1,2,3,4,5)
tuple_fruits_name=("orange","mango","cherry")

print("Value of tuple : ",tuple_value)
print("Data type of tuple: ",type(tuple_value))

print("Value of tuple fruits name : ",tuple_fruits_name)
print("Data type of tuple fruits name : ",type(tuple_fruits_name))

tuple_add=tuple_value+tuple_fruits_name
print("Value of tuple_add: ",tuple_add)
print("Data type of tuple add : ",type(tuple_add))


