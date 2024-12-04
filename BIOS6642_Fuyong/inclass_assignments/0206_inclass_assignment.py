entry = 1 # Ensure the loop is entered
sum_value = 0 # Initialize sum
count = 0 # Count valid values

# Request input from the user
print("Please enter values, zero ends list:")
while entry != 0: # A zero exits the loop
    entry = float(input()) # Get the value
    if entry > 0: # Is value positive?
        if count == 0:
            # The first iteration
            max_value = entry
            min_value = entry
        else:
            # Update max_value and min_value if necessary
            if max_value < entry:
                max_value = entry
            if min_value > entry:
                min_value = entry
        sum_value += entry # Only add it if it is positive
        count += 1 # Only count it if it is positive

if count == 0:
    print('No positive values provided.')
else:
    print('Average of positive values: ', sum_value/count)
    print('Maximum positive value: ', max_value)
    print('Minimum positive value: ', min_value)