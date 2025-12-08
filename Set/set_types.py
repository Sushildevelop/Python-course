# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.

set_fruits={"orange","mango","banana"}

set_fruits_price={50,60,80}

print("Value of set fruits :",set_fruits)
print("Data type of set fruits :",type(set_fruits))

print("Value of set fruits price :",set_fruits_price)
print("Data type of set fruits price :",type(set_fruits_price))

set_add=set_fruits_price | set_fruits
print("Value of set fruits add  :",set_add)
print("Data type of set fruits add  :",type(set_add))

