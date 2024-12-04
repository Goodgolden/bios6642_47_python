# Get input values from user
print("Please enter four integer values.")
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

# Compute the maximum and minimum values
max_num = num1
if num2 > max_num:
    max_num = num2
if num3 > max_num:
    max_num = num3
if num4 > max_num:
    max_num = num4

min_num = num1
if num2 < min_num:
    min_num = num2
if num3 < min_num:
    min_num = num3
if num4 < min_num:
    min_num = num4

# Report results
print("The maximum number entered was:", max_num)
print("The minimum number entered was:", min_num)
