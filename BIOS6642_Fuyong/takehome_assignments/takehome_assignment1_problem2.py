# Get row and colum values from user
row = int(input('Enter row: ')) # It is an inetger
column = int(input('Enter column: ')) # It is an inetger

if row > 1 and column > 1: # assume at least 2 rows and columns
    print('+ ' + '- ' * (column - 2) + '+') # Print the first row
    for idx in range(row - 2):
        print('| ' + '  ' * (column - 2) + '|') # Print the middle
    print('+ ' + '- ' * (column - 2) + '+') # Print the last row
else:
    print('At least 2 rows and 2 columns!')
