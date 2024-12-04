#Question 1
##Method 1
height = int(input("Please enter the level of the tree: "))
row = 1
for row in range(height+1):
    for count in range(height-row+1):
        print(end=' ')
    for count in range(height-row+1, height+1):
        print(end='*')
    print()
for row in range(height+1, 2*height+1):
    for count in range(row-height+1):
        print(end=' ')
    for count in range(row-height+1, height+1):
        print(end='*')
    print()

##Method 2
height = int(input("Please enter the level of the tree: "))
for row in range(1, height+1):
    uptree = " "*(height-row) + "*"*row
    print(uptree)
for row in range(height+1, 2*height):
    downtree = " "*(row-height) + "*"*(2*height-row)
    print(downtree)
print()

#Question 2
row = int(input("Please enter the level of the rows (>=2): "))
col = int(input("Please enter the level of the colums (>=2): "))
print("+ ", "– "*(col-2), "+", sep="")
for count in range(2, row):
    print("| ", "  "*(col-2), "|", sep="")
print("+ ", "– "*(col-2), "+", sep="")
