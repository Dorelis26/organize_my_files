import os

file_path = "C:/Users/dorel/Downloads/Screenshot_20221211-222026_Instagram.jpg"
print(file_path)

if os.path.isfile(file_path):
    os.remove(file_path)
    print("file has successfully been deleted!!")
else:
    print("this file does NOT exist!!!")

