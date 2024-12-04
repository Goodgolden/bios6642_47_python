import sys

def move_object(x):
    if x == 1 or x == 2:
        return x
    else:
        return move_object(x-1) + move_object(x-2)

# Usage (command line): python 0305_inclass_assignment.py 6
if __name__ == '__main__':
    print('There are {0} distinct ways to move the object to the position, {1}'.format(move_object(int(sys.argv[1])), int(sys.argv[1])))