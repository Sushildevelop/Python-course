# Bitwise Operators

# Bitwise operators are used to compare (binary) numbers

# It works on bits and performs bit by bit operation

#       Operator	Name	                Example
#         &	        AND	                    x & y
#         |	        OR	                    x | y
#         ^	        XOR	                    x ^ y
#         ~	        NOT	                    ~x
#         <<	    Zero fill left shift	x << 2
#         >>	    Signed right shift	    x >> 2

x=10  # Binary: 1010
y=4   # Binary: 0100


print("Bitwise AND: ", x & y)   # Binary: 0000 => Decimal: 0
print("Bitwise OR: ", x | y)    # Binary: 1110 => Decimal: 14


print("Bitwise XOR: ", x ^ y)   # Binary: 1110 => Decimal: 14

# Rule of XOR:

# 1 ^ 1 = 0

# 0 ^ 0 = 0

# 1 ^ 0 = 1

# 0 ^ 1 = 1

# It means:

# “If bits are different → 1, if same → 0”


print("Bitwise NOT: ", ~x)      # Binary: ...11110101 => Decimal: -11
# First remember:
# x = 10
# Binary of 10 (in 8-bit form) = 00001010

# Bitwise NOT (~) means:

# It flips every bit
# 0 becomes 1, and 1 becomes 0

#   x  = 00001010
#   ~x  = 11110101
# Now this binary number starts with 1, which means it is a negative number in Python (because Python uses two’s complement for signed integers)



print("Zero fill left shift: ", x << 2)  # Binary: 101000 => Decimal: 40
# Left shift means:

# Shift all bits to the left and fill new spaces with 0

# x = 10 → Binary 1010

# Each left shift = multiply by 2
# So shifting by 2 = multiply by 4

# 10 × 4 = 40

# Binary 101000 = Decimal 40


print("Signed right shift: ", x >> 2)     # Binary: 0010 => Decimal: 2
# Binary 0010 = Decimal 2

# Each right shift = divide by 2
# So shifting by 2 = divide by 4

# 10 ÷ 4 = 2
