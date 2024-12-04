import sys

def reverse_integer(x):
    result, is_positive = 0, 1
    if x < 0:   # If x is negative, convert it to be positive
        is_positive = -1
        x = -1 * x
    while x != 0:
        result = result * 10 + x % 10   # Extract the last digit and add it to result's current value each time
        x //= 10
    return result * is_positive

# Usage example (command line): python takehome_assignment2_problem1.py 230
if __name__ == "__main__":
    print(reverse_integer(int(sys.argv[1])))
