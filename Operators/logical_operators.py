#Logical Operators 

# Logical operators are used to combine conditional statements
#Return - True or False

#       Operator	Name	        Example
#         and	    Logical AND	    x < 65 and  x < 100   # Both conditions must be true
#         or	    Logical OR	    x < 20 or  x < 25     # At least one condition must be true
#         not	    Logical NOT	    not(x < 56)


x=10

print("Logical AND: ", x > 5 and x < 15)  
print("Logical OR: ", x > 5 or x < 5)      
print("Logical NOT: ", not(x > 5 and x < 15))  