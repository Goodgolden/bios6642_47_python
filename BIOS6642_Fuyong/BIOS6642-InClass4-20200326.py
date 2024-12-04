string=input("please provide your string: ")
my_string=string.lower()

def check(b):
    for i in range(1, len(b)):
        if b[i-1]!=b[i]:
            continue
        elif b[i-1]==b[i]:
            b=b[0:i-1]+b[i+1:]
            check(b)
    print("this is the final result: ", b)
check(my_string)
