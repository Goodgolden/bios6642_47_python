### Question1
from math import log10 # use the log10 function is more efficent than the while loop
n=int(input("Please provide an integer: "))
rev=0 # start with a fresh beginning
if n>0: # condition for positive integer
    m=int(log10(n)) # how many digits in the integer.
    for i in range(0, m+1):
        d=n//10**(m-i) # to get one digit each time, from high to low
        rev=d*(10**(i))+rev # to add the exact digit from last step, from low to high
        n=n%(10**(m-i)) # to get the second highest digit of the
elif n<0: # condition for negative integar
    n=-n # temperarily change the sign
    m=int(log10(n))
    for i in range(0, m+1):
        d=n//10**(m-i) # to get one digit each time, from high to low
        rev=d*(10**i)+rev # to add the exact digit from last step, from low to high
        n=n%(10**(m-i)) # to get the second highest digit of the
    rev=-rev #change the sign back
# if n=0, then we do not need to do anything
print("Your result is:", rev)

### Question2
p1=int(input("Please provide a positive integer: \n"))
p2=int(input("Please provide a larger positive integer: \n"))
if (p1>=p2) or p1<=0 or p2<=0: # if the requirement is mot meet, there will be warning message.
    print("Are you kidding? Do it again")
else:
    print("Here are your results: ")
    for p in range(p1, p2+1): # this statement will include p2
        n=p # because p is need to be used later, so assign the value of p to n
        for i in range(0, int(log10(p))+1): # to extract each digit in the integer n
            r=n//10**(int(log10(p))-i) # and assign the digit to r, from the highest to lowest
            n=n%10**(int(log10(p))-i) # can also be coded with round(p, -m-i+1)
            if r==0: # 0 cannot be the denominator
                break # but the remainder is still 0, so just continue
            else: # for the case of nonzero,
                if p%r == 0: #p is dividable by r then we can test the next highest digit.
                    if i==int(log10(p)):  # if and only if all p can be divided by all of the digits
                        print(p)
                else: # as long as there is one digit does not work, the program will break
                    break
