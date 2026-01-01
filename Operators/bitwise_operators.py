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
print("Bitwise NOT: ", ~x)      # Binary: ...11110101 => Decimal: -11
print("Zero fill left shift: ", x << 2)  # Binary: 101000 => Decimal: 40
print("Signed right shift: ", x >> 2)     # Binary: 0010 => Decimal: 2
