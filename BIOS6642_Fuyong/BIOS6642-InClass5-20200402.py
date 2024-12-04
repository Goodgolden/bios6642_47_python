lst=input("please provide your list: ")
lst=list(lst.split(','))
lst.sort(key=str.lower)
print(lst)

def prefix(lst):
    prefix=lst
    for item in lst:
        if len(prefix)>len(item):
            prefix=item
        else:
            continue
    return prefix

def clean(lst):
    for item in lst:
        if item[0:len(prefix(lst))]==prefix(lst):
            continue
        else:
            lst.remove(item)
    return lst

def game(lst):
    pre=prefix(lst)
    i=0
    while i in range(0, len(clean(lst))):
        if fnmatch.fnmatch(lst[i], pre):
            pre=lst[i]+"?"
            i=i+1
        else:
            break
    print(lst[i-1], pre)

game(lst)
