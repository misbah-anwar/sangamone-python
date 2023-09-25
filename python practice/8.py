def dm1(word1):
    name=word1
    len1=len(name)
    for i in range(1,len1+1,1):
        print(name[0:i])
    for i in range(1,len1,1):
        print(name[0:len1-i])
dm1("Misbah")