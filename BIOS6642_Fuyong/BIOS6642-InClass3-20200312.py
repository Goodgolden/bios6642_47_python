def check_string(b):
    a=""
    if len(b)==0:
        print("True")
    elif ((b[0]=="[") or (b[0]=="(")):
        for i in range(0, len(b)):
            if (b[i]=="[") or (b[i]=="("):
                a=a+b[i]
                if len(a)==len(b):
                    print("False")
                    break
                elif (len(a)==0) and (len(b)!=0):
                    check_string(b)
            else:
                if ((a[len(a)-1]=="(") and (b[i]==")")) or ((a[len(a)-1]=="[") and (b[i]=="]")):
                    a=a[0:len(a)-1]
                    b=a+b[i+1:len(b)]
                    check_string(b)
                else:
                    print("False")
                    break
    else:
        print("False")

my_string=input("pleas provide a string contains only [, ], (, ): ")
check_string(my_string)
