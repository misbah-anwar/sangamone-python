with open("in1.txt")as file:
    list1=file.readline().split(',')
    start=int(list1[0])
    end=int(list1[1])

with open("out.txt","w")as file1:
    for i in range(start,end+1):      
            for j in range(1,11):
                str1=str(i)+"*"+str(j)+"="+str(i*j)
                print(str1)
                file1.write(str1)
                file1.write("\n")
            print()
            file1.write("\n")