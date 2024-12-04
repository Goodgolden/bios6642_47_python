from random import randrange

def guess_num(max_num, rand_num):
	first = 0
	last = max_num
	count = 0
	while first <= last:
		count += 1
		mid = (first + last) // 2 # Always guess the number in the middle between first and last
		if mid == rand_num: # If it correctly finds the number, stop searching
			print('Find the random number!')
			break
		else:
			if rand_num < mid: # The number is in the first half
				last = mid - 1
			else: # The number is in the second halfs
				first = mid + 1
	return count

# Usage (command line): python takehome_assignment3_problem1.py
if __name__ == '__main__':
	max_num = 1000
	rand_num = randrange(1, max_num+1)
	print('It takes {0} guesses to find {1}.'.format(guess_num(max_num, rand_num), rand_num))
