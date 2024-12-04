import sys

def integer_break(num):
    if num == 2: # 2 = 1 + 1, then 1 * 1  = 1
        return 1
    if num == 3: # 2 = 1 + 2, then 1 * 2  = 2
        return 2
    max_prod = 1
    while num > 4: # For any num > 4, repeatedly extract 3 because product of 3's will is maximum.
        max_prod *= 3
        num -= 3
    return max_prod * num

# Usage (command line): python takehome_assignment3_problem2.py 10
if __name__ == '__main__':
    print('For integer {0}, the maximum product is {1}.'.format(int(sys.argv[1]), integer_break(int(sys.argv[1]))))
