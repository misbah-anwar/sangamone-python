import os
def search_virus(search_path,target):
    for root, dirs, files in os.walk(search_path):
        for file_name in files:
            if file_name.endswith(".txt"):
                file_path=os.path.join(root,file_name)
                with open(file_path,'r',encoding='utf-8',errors='ignore')as file:
                    content=file.read()
                    if content.lower().count('devil')==target:
                        return file_path

target=4
drives = ["C:","D:"]

found_file = False

for drive in drives:
    if os.path.exists(drive):
        try:
            file_path = search_virus(drive, target)
            if file_path is not None:
                print(f"Found file with 'devil' mentioned {target} times at: {file_path}")
                found_file = True
                break
        except Exception as e:
            print(f"An error occurred while searching in {drive}: {e}")
    else:
        print(f"Drive {drive} does not exist.")
        
if not found_file:
    print(f"No file found with 'devil' mentioned {target} times.")
