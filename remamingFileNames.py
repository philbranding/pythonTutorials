import os

def rename_files():
    # 1 get file names from a folder
    saved_path = os.getcwd()
    file_list = os.listdir(saved_path+"/prank")
    print(file_list)

    print("Current working Directory is " + saved_path)
    os.chdir(r"/Users/phil/WebDev/Udacity/00-Python/BasicPython/00-Projects")
    # 2 for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.strip("01234567789"))
        os.chdir(saved_path)
rename_files()