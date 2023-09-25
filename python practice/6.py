import os
import datetime as dt
output_dir="TABLES"
now=dt.datetime.now()
fname1="hello_"
fname21=str(now.year)
fname22=str(now.month).zfill(2)
fname2=fname21+fname22
fname3=".txt"
fname=fname1+str(fname2)+fname3
print(fname)
os.makedirs(output_dir,exist_ok=True)
with open("hello.txt","w")as file1:
    print()
