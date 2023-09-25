with open("in.txt")as file:
    start=int(file.readline())
    end=int(file.readline())

for i in range(start,end+1):      
        for j in range(1,11):
            print(f"{i}*{j}={i*j}")
        print()