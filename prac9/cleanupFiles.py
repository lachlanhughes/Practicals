"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import os, shutil

__author__ = 'Lindsay Ward'

print("Current directory is", os.getcwd())

# change to desired directory
os.chdir('Lyrics/Christmas')
# print a list of all files (test)
# print(os.listdir('.'))

# make a new directory
# os.mkdir('temp')

# loop through each file in the (original) directory
for filename in os.listdir('.'):
    # ignore directories, just process files
    if not os.path.isdir(filename):

        new_name = ""
        for i, letter in enumerate(filename):
            try:
                if letter.islower() and filename[i+1].isupper():
                    new_name += letter
                    new_name += "_"
                else:
                    new_name += letter
            except IndexError:
                new_name += filename[-1]

        new_name = new_name.replace(" ", "_").replace(".TXT", ".txt")

        new_new_name = ""
        for i, letter in enumerate(new_name):
            try:
                if letter == "_" and new_name[i+1].islower():
                    new_new_name += "_"
                    new_new_name += new_name[i+1].upper()
                else:
                    new_new_name += letter
            except IndexError:
                new_new_name += letter



        print(new_new_name)

        # Option 1: rename file to new name - in place
        # os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        # shutil.move(filename, 'temp/' + new_name)


# Processing subdirectories using os.walk()
# os.chdir('..')
# for dir_name, subdir_list, file_list in os.walk('.'):
#     print("In", dir_name)
#     print("\tcontains subdirectories:", subdir_list)
#     print("\tand files:", file_list)

