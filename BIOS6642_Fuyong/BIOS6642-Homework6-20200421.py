### Question1
number=input("Please provide a integer number: ") # take the input integer list
k=int(input("The number you want to remove: ")) # take the number of integers to remove

def game1(number, k):
    new=[] # a list for the number
    n=len(number)
    if n==k: # in the case of every integer is removed
        return "0"
    for d in number: # iteration of every number
        if k and new and new[-1]>d: # if the next number is small
            new.pop() # remove the last integer, because it decreasing
            k-=1 # after the removing of the number
        new.append(d) # make the new list which is increasing
    if k>0 : # need further removing
        new.pop() # remove the last number
        k-=1
    return "".join(new).lstrip("0") or "0" # return the value

game1(number, k)

##########################################################################
### Question2
listA=list(input("Please provide the words: ").split()) # take the input string list
str1=input("Please provide string1: ") # take the string 1
str2=input("Please provide string2: ") # take the string 2

def game2(listA, str1, str2):
    word=[] # a list for the words has str1 and str2
    result=-1 # set result as -1
    length=len(listA) # iteration of the words list
    for index in range(0, length):
        prefix = (listA[index][:len(str1)]==str1) # check the prefix and suffix
        suffix = (listA[index][len(listA[index])-len(str2):len(listA[index])]==str2)
        if (prefix!=0) and (suffix!=0):
            word.append(listA[index]) # add the word or pop out the old word
            result=index # update the index
    if word!=[]: # there are words share the prefix or suffix
        print("Your result is the index[", result, "] word in the list: ", word[-1], sep="")
    else: # if no word fit for the prefix and suffix, just return -1
        return result

game2(listA, str1, str2)

##########################################################################
### Question3
string=input("Please provide a sequence of integer number: ")
numbers=list(map(int, string.split()))

def game3(nums):
    tails = [0] * len(nums) # set tails for rearranging the increasing order
    size = 0 # starting with the first position of the tails
    for x in nums: # iteration of each integer in the string
        i=0
        j=size # this is the size
        while i!=j:
            print("i:", i, " j:", j, "x=", x, " string=", tails, sep="")
            m = (i+j)//2 # binary, dichomize the find the position m
                        # compare to word m
                        # then dichomize the i to j position for new m
                        # until find the position of x
            if tails[m]<x: # if the new integer x smaller,
                i=m+1 #
            else:
                j=m # the size gonna be the
        tails[i]=x # put the new integer x in a new position in tails
        size=max(i+1, size) # the size depends on whether the new integer x
                            # will replace the earlier one
    print("Here is the subsequence containing", size, "elements.")

game3(numbers)
