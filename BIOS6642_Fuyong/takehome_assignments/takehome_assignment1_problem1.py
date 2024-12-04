# Get tree level from user
level = int(input('Enter level of tree: '))

# Draw one row for each level at a time
for row in range(1,2*level):
    if row < level + 1: # The first half
        # Print the first half of the tree
        print(' ' * (level - row) + '*' * row)
    else:
        # Print the second half of the tree
        print(' ' * (row - level) + '*' * (2*level - row))
