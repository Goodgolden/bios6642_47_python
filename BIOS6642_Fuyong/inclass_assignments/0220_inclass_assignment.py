import sys

def count_string(str1,str2):
    """ This functions has two parameters: count_string(str1, str2).
    It computes and returns the number of a specific substring, str2, in another string, str1.
    """
    count = 0
    for idx in range(len(str1) - len(str2) + 1):
        if str2 == str1[idx:idx+len(str2)]: # Check if str2 is equal to the current substring in str1
            count = count + 1
    return count

# Usage with command line: Python 0220_inclass_assignment.py banana na
if __name__ == "__main__":
    print(count_string(sys.argv[1], sys.argv[2]))
