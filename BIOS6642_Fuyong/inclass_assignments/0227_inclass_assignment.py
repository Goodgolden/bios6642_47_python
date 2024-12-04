########### This program is tested on MacBook

from random import randrange
from time import time

rand_num = randrange(1, 101)
n = 0
count = 0

time_start = time()
while n >= 0:
    n = int(input('Please enter an integer betwee 1 and 100: '))
    if n < 0:
        print('Quit the game without a correct guess.')
        time_elapsed = time() - time_start
        break

    count += 1
    if n == 0:
        time_start = time()
        count = 0
        print('You have reset the guess!')
    elif n == rand_num:
        print('Correct!')
        time_elapsed = time() - time_start
        break
    elif n > rand_num:
        print('The integer you provided is too high.')
    else:
        print('The integer you provided is too low.')

print('Number of guesses: ', count)
print('Time elapsed: ', round(time_elapsed, 2), 'seconds.')
