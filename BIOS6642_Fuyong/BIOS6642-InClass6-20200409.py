def wordcounter(filename):
    counters={}
    with open(filename, "r") as file:
        content=file.read()
        word_set=content.split()
        for word in word_set:
            word=word.replace(",", "")
            word=word.replace(".", "")
            if word not in counters:
                counters[word]=1
            else:
                counters[word]+=1
    for word, count in counters.items():
            print(word,count)
    print("-+"*20)
    for word, count in counters.items():
            if word in ("people", "right"):
                print(word, count)




wordcounter("document.txt")
