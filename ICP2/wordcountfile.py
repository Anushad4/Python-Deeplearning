file=open("test.txt","r")
wordcount={}
for word in file.read().split():
    if word.casefold() not in wordcount:
        wordcount[word.casefold()] = 1
    else:
        wordcount[word.casefold()] += 1
#print(wordcount)
f=open("words.txt","w")
#f.write(str(wordcount))
for k,v in wordcount.items():
    #for k, v in f.write(str(wordcount)) :
    #print (k,v)
   f.write('%s:%s\n' %(k,v))
file.close();

