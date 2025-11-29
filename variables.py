# name="sushil"
name='sushil'
name=20
#Type casting
# last_name=str(name)
# print(last_name)
# print(type(last_name))
# print(name)

# explore more about variables and data types in python
x=10,
# print(type(x))
# y=str(x)
# print("y-->",y)
# print(type(y))
# y=10,
# z=10,

x=y=z=10
# print(x,y,z)
# list_of_numbers=[1,2,33,44]
# print(list_of_numbers)
# fruits=["apple","banana","mango"]
#int , str , float 

# print(fruits)

a=10
b=20
c=a+b
# print(c)


#Global variable 
global_var=100
local_var=300
def my_function():
    #Local variable
    local_var=200
    print("Inside function:",local_var)
    print("Inside function with global variable:",global_var)

my_function()
print("Outside function:",global_var)
print("Outside function:",local_var)



