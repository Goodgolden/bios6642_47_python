###Question1:
lst=input("please provide your list of integers, seperate with space: ")
length=int(input("please provide your positive integer: "))
avg=int(input("please provide your average integer: ")) # to take the inputs
lst=list(lst.split()) # split the string of numbers into list
lst=list(map(int, lst)) # converge the numbers in the list into integers

def game2(lst, length, avg): # define a function
    from itertools import combinations # need to use the combination tool
    time=0 # start with zero times, this will record each correct result
    comb=combinations(lst, length) # the comb contain all the sublist
    sumup=avg*length # to get the sum of the critical value
    print("\nHere are the correct results: ")
    for each in list(comb): # for loop to test each sublist in comb
        addup=0 # sum up the elements in the sublist with "length" elements
        for i in range(0, length): # iteration to get the elements in the "length" sublist
            addup+=each[i]  # sum up the elements in the sublist with "length" elements
        if addup>=sumup: # the correct result: sum of sublist is larger than critical value
            print(each) # print out the final result
            time+=1 # add one more time to the correct answer
        else: # the alternative condition, if the sum of sublist smaller than the critical
            continue # just continue and get to the next set of sublist
    print("The answer is: ", time) # finally print out the correct answer

game2(lst, length, avg) # here you go

###Question2:
lst1=input("please provide your list of integers, seperate with space: ")
lst1=list(lst1.split()) # split the string of numbers into list
lst1=list(map(int, lst1)) # converge the numbers in the list into integers

def game3(lst): # define a new game function
    lst2=[0]*len(lst) # set up the lst2 as a list with all the zeros
    for i in range(0, len(lst)-1): # no matter what the last element is "0"
        for j in range(i+1, len(lst)): # this will make sure j is not empty
            if lst[i]<lst[j]: # if the jth is larger than the ith
                lst2[i]=j-i # just calculate the distance
                break # then the program will stop for the ith, and move on
            else: # if the ith element is the largest one,
                continue # then we do not need to change the value "0" in lst2
    print("This is your result: ", lst2) # finally we can print out lst2

game3(lst1) # test of example 1 in the assignment

###Quesiton3:
lst3=input("please provide your string: ")
lng=int(input("please provide the length: "))

def unique(string): # define a new function to check the uniqueness of each letter
    for i in range(0, len(string)): # for loop to check each ith element
        for j in range(i+1, len(string)): # comparing with the jth element
            if string[i]==string[j]: # if the same of ith and jth
                return False # return the value as False
                break # breakthe loop and stop
    return True # otherwise if the loop is finished return True

def game4(lst, lng): # define the game function
    if lng>len(lst): # check the condition, otherwise no substring
        print("the string is too short; the answer is: 0")
    else: # if the length of string larger than requirment
        time=0 # clear off the number of successes
        print("here are the results:") # print out substring and uniqueness
        for i in range(0, len(lst)-lng+1): # generate each substring
            print(lst[i:i+lng], unique(lst[i:i+lng])) # the results
            if unique(lst[i:i+lng])!=False: # find the substring
                time+=1 # which has no letter repeated
        print("the answer is: ", time) # finally print out the answer

game4(lst3, lng)
