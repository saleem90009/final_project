
x = str(input("enter your first name"))
y = str(input("enter your middle name"))
z = str(input("enter your last name"))
# 1. Concatenate the three inputs and use (-) to separate between them.
name = (x+"-"+y+"-"+z)
print(name)
# 2. Split the result in n1. Task. Then print the result as list .
print(name.split("-"))


x = int(input("enter first value"))
y = int(input("enter second value"))
# 1.Return the addition of the numbers
print("addition= ")
print(x+y)
# 2.Return the subtraction of the numbers
print("subtraction= ")
print(x-y)
# 3.Return the multiplication of the numbers
print("multiplication= ")
print(x*y)
# 4.Return the normal division of the numbers
print("division= ")
print(x/y)
# 5.Return the integer division of the numbers
print("integer division= ")
print(int(x/y))
# 6.Return the exponential of the numbers , suppose a number to be the power.
print("exponential= ")
print(x**y)
