from random import randrange
from time import perf_counter
random=randrange(1, 101)
time=0
ans=False
start=perf_counter()
while ans==False:
    user=int(input("please give me your guess: "))
    if user<0:
        break
    elif user==0:
        ans=False
        time=0
        start=perf_counter()
        elapsed=0
    else:
        if user>random:
            print(user, " is too large!")
            ans=False
            time+=1
        elif user<random:
            print(user, " is too small!")
            ans=False
            time+=1
        elif user == random:
            ans=True
            print("congratulations!!! after ", time, "wrong guesses, you get the corret answer!")
        elapsed = perf_counter()-start
    elapsed = perf_counter()-start
    print("Totally you used", elapsed, "seconds")
