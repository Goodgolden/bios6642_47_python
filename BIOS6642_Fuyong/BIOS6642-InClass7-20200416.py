with open('citations.csv') as file:
    d={}
    next(file)
    for line in file:
        mylist=line.split(",")
        name=mylist[0]
        paper=mylist[1:len(mylist)]
        paper=[int(a) for a in paper]
        paper.sort(reverse=True)
        print(name, paper)
        for i in range(len(paper)):
            if paper[i]>=i+1:
                index=i+1
            else:
                index=index
        d[name]=index
    for k, v in d.items():
            print(k, v)
            print("Done!")

def find(author, dictionary):
    try:
        index=dictionary[author]
        print(author, index)
        print("Done!")
    except ValueError:
        print('Cannot convert integer')
    except Exception:
        print('This name does not exist')


find("Mia", d)
find("Randy", d)
