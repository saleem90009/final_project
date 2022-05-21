x = input("enter your first_name")
y = input("enter your middle_name")
z = input("enter your last_name")


def print_name(first_name, middle_name, last_name):
    return str(first_name) + "-" + str(middle_name) + "-" + str(last_name)


print("my name is : " + print_name(first_name=x, middle_name=y, last_name=z))

# 2. Split the result in n1. Task. Then print the result as list .
b = print_name(first_name=x, middle_name=y, last_name=z)
full_name = str(b)
print(full_name.split("-"))

