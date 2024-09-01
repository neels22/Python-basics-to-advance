

# what if we want to open every file in a directory 
# what if we want to move files around on out computer 
# os and shutil module allow us to do this moving and deleting them
# shutil -- shell utilities
# pwd - present working directory 
# 


import os 
import shutil

os.getcwd() # -- get the current working directory 

os.listdir() # -- return a list of  everything in my currect directory  -- you can pass the file name and it will list only files from that file

#shutil.move('testfile.txt','/Users/indraneelsarode/Desktop/Python-basics-to-advance/Unit_testing')  # takes two para -- source and destination


# ways to delete a file

# os.unlink('path') # - which delete a file at the path you provide
# os.rmdir('path') # - which deletes a folder at the path you provide
# shutil.rmtree('path') # -- this is dangerous as it will remove everything 

# all these methods cant be reversed you wont find it in trash

# instead we will use send2trash module external module

import send2trash

# shutil.move('Unit_testing/testfile.txt',os.getcwd())

print(os.listdir())

# send2trash.send2trash('send2trash.txt')

# os.walk() # - dir tree tuple 

filepath = 'Milestone_projects'

for folder , subfolders, files in os.walk(filepath):
    print(f"currently looking at {folder}")
    print('\n')
    print('for every subfolder')
    for sub_fold in subfolders:
        print(f"subfolder {sub_fold}")

    print('\n')

    print('the files are ')
    for f in files:
        print(f" files are {f}")
    print('\n')
