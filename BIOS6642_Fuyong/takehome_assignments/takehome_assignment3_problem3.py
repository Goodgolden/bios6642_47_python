import sys

def longest_substring_length(str1):
    max_length = 0
    for idx in range(len(str1)):
        count = 0
        current_subtring = '' # The current substring
        for cur_char in str1[idx:]:
            if cur_char not in current_subtring: # Check whether cur_char is unique in current_subtring
                current_subtring += cur_char
                count += 1
                if max_length < count: # Record the length of the current longest substring
                    max_length = count
            else:
                break
    return max_length

# Usage (command line): python takehome_assignment3_problem3.py asdfsab
if __name__ == "__main__":
    print(longest_substring_length(sys.argv[1]))
