def dm2(file1):
    def dm1(word1):
        name=word1
        len1=len(name)
        for i in range(1,len1+1,1):
            print(name[0:i])
        for i in range(1,len1,1):
            print(name[0:len1-i])
    f1=open(file1,"r")
    for i in range(0,6,1):
        name1=f1.readline()
        dm1(name1)
dm2("in4.txt")