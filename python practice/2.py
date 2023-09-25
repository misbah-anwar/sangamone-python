start=int(input("enter start: "))
end=int(input("enter end: "))

for i in range(start,end+1):
    try:        
        for j in range(1,11):
            print(f"{i}*{j}={i*j}")
        print()
    except Exception as e:
       print(f"an error has occured: {e}")