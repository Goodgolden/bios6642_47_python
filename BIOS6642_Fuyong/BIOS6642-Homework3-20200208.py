# BIOS6642 Homework3
# Question1:
from random import randrange # get the random selection function
def maxproduct(x): # define the function "maxproduct"
    if x<=3: # if the value we select is 2 the result will be 1;
             # if the value we select is 3 the result will be 2.
        product=x-1
    # for any integer >4, the product of 2 or 3 will be the larger than other combinations
    # for example: 5=3+2, 3*2=6 is the largest product
    elif x%3==0:
        product=3**(int(x/3))
    # for any integer >3 we do not want any 1 in the split
    # so if x%3==1, we want the number to be 4 other than 1
    elif x%3==1:
        product=4*3**(int(x-1)/3-1)
    # for maximum product, we want as more 3 as possible
    # for example: we want 3*3=9 other than 2*2*2=8
    else:
        product=2*3**(int(x-2)/3)
    return int(product)

random=randrange(2,50)
print("Your random integer is: ", random)
print("Your max product is: ", maxproduct(random))


# Question2:
from random import randint # get the random selection function
def game(): # define a function with this guess game
    number=randint(0, 1000) # randomly generate a integer from 1 to 1000
    high=1000 # start with high bound
    low=0 # and a low bound
    guess=high # every time dichotomize the range the first try start with 500
    time=0 # start with time with 0
    while guess!=number: # run the program until guess==number
        if guess>number: # guess is bigger than the variable
            high=guess # set the high bound as the guess
            guess=int((low+high)/2) # dichotomize the range again
            time=time+1 # time increase 1
            print("we have tried", time, "times; my guess was", guess)
        elif guess<number: # guess is bigger than the variable
            low=guess # set the low bound as the guess
            guess=int((low+high)/2) # dichotomize the range again
            time=time+1 # time increase 1
            print("we have tried", time, "times; my guess was", guess)
    print("Finally after", time, "times, we get correct answer", number)


game()


# Question3:
def substring(str1): # define the function substring
    i=0 # index of each letter from the input string
    str2="" # start with empty string, the new letters will be add to substring
    for letter in str1: # traversal with a for loop
        i+=1 # iterations and check all the letters after ith letter
        if str1.find(letter, i)<0: # check whether the ith letter repeated later
            str2=str2+letter # if it never repeats, add it into the substring
        elif str1.find(letter, i)>0: # if the ith letter repeats,
            str2="" # clean the substring and start it over
    print("Here is your string:", str2) # print out the substring


str1=str(input("Please put your string here: "))
substring(str1) # can also be achieved with rfind function
