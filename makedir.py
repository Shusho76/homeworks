import os

os.makedirs("New_dir/Dir_1")
print("I create this dir")
os.chdir("New_dir")
os.makedirs("Dir_1/Dir_2")
os.makedirs("Dir_1/Dir_3")
print("I create thees folders")
open("Text.doc","a")
print("In New_dir directory created new Text.doc.file")

delate_directory = input("Do you want to delate all created folders? Y/N\n")
if delate_directory == "Y":
    os.chdir("Dir_1")
    os.rmdir("Dir_2")
    os.rmdir("Dir_3")
    os.chdir("../..")   
    os.rmdir("New_dir/Dir_1")
    os.chdir("New_dir")
    os.remove("Text.doc")
    os.chdir("..")
    os.rmdir("New_dir")

    print("All created folders and files were deleted")

else:
    print("Continue working")