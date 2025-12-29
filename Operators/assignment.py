
# Assignment operators are used to assign values to variables

#     Operator	            Example	                  Same As	
#     =	                    x = 5	                    x = 5	
#     +=	                x += 3	                    x = x + 3	
#     -=	                x -= 3	                    x = x - 3	
#     *=	                x *= 3	                    x = x * 3	
#     /=	                x /= 3	                    x = x / 3	
#     %=	                x %= 3	                    x = x % 3	
#     //=	                x //= 3	                    x = x // 3	
#     **=	                x **= 3	                    x = x ** 3	
#     &=	                x &= 3	                    x = x & 3	
#     |=	                x |= 3	                    x = x | 3	
#     ^=	                x ^= 3	                    x = x ^ 3	
#     >>=	                x >>= 3	                    x = x >> 3	
#     <<=	                x <<= 3	                    x = x << 3

# 1. = (Assign)

# Assigns a value to a variable
x=5 
print(x)  #5 

# 2. += (Add and Assign)

# Adds a value to the variable and stores the result back in the same variable.
y=10
y+=3  # y=y+3
print("Value of y ---> ",y)



# 3. -= (Subtract and Assign)

# Subtracts a value from the variable and assigns the result back.

z=10
z-=3   #z=z-3
print(z)

# 4. *= (Multiply and Assign)

# Multiplies the variable and stores the new result.
a=10
a*=3   # a=a*3

print(a)



# 5. /= (Divide and Assign)

# Divides the variable and stores the floating result.

b=20
b/=4   #b=b/4
print(b)


# 6. %= (Modulus and Assign)

# Finds remainder and updates the variable with that remainder.

c=21
c%=4   # c=c%4  # 21/4=5 remainder=1
print(c)

# 7. //= (Floor Divide and Assign)

# Performs floor division (integer division) and assigns result.

d = 17
d //= 3  # d = d // 3   # 17/3=5.66 => floor value=5
print(d)


# 8. **= (Exponent and Assign)

# Raises the variable to a power and assigns result.

p=5
p**=2   #p=p**2   = 5*5
print(p)


# 9. &= (Bitwise AND and Assign)

# Applies bitwise AND operation and updates the variable.

h = 7      # binary 111       
h &= 3     # binary 011
print(x)   # 3   

#   111   (7)
# & 011   (3)
# -------
#   011   (Result = 3)




# 10. |= (Bitwise OR and Assign)

# Applies bitwise OR and updates the variable.

k=7   
k|=3
print(k)

#   111   (7)
# | 011   (3)
# -------
#   111   (Result = 3)



# 11. ^= (Bitwise XOR and Assign)

# Applies XOR (exclusive OR) and updates the variable.

l = 6      # 110
l ^= 3     # 011
print(x)   # 5 (101)

#   110   (6)
# | 011   (3)
# -------
#   101   (Result = 5)




# 12. >>= (Right Shift and Assign)

# Right-shifts bits of the variable and updates it.

x = 16     # 10000
x >>= 2
print(x)   # 4 (100)


# 13. <<= (Left Shift and Assign)

# Left-shifts bits of the variable and updates it.
z=16   # 10000
z<<=2      
print(z)   # 64 (1000000)
