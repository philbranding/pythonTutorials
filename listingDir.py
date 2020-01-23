import os

def get_directory_name():
    saved_path = os.getcwd()
    file_list = os.listdir(saved_path+"/prank")
    print(file_list[3])


get_directory_name()