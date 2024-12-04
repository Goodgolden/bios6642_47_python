def is_valid(bracket_string):
    current_list = []
    for i in range(len(bracket_string)):
        if bracket_string[i] == '(' or bracket_string[i] == '[':
            current_list.append(bracket_string[i])
        if bracket_string[i] == ')':
            if current_list == [] or current_list.pop() != '(':
                return False
        if bracket_string[i] == ']':
            if current_list == [] or current_list.pop() != '[':
                return False
    return False if current_list else True

bracket_string = input('Please enter a string containing only (,),[,]: ')
print(bracket_string+':', is_valid(bracket_string))
