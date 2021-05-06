def countWordsFromFile():
    filename=input("Enter the file name") 
    noOfWords=0

    file=open(filename,'r')
    for line in file:
       words=line.split()
       noOfWords=noOfWords+len(words)
    print("noOfWords")
    print(noOfWords)

countWordsFromFile()