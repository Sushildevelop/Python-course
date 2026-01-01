# Identity operators are used to compare the objects, not if they are equal,
# but if they are actually the same object, with the same memory location.


# It's returns True or False

#       Operator	Name	        Example
#         is	    Identity	    x is y          
#         is not	Not Identity	x is not y

x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry"]

a=x

print("a is x: ",a is x)    # Because a references the same object as x  
print("x is y: ",x is y)

print("x is not y: ",x is not y)
