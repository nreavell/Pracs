"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import shutil
import os


def main():
    dir_names = {}
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('FilesToSort')
    # print a list of all files (test)
    print(os.listdir('.'))

    # make a new directory
    # os.mkdir('temp')

    # loop through each file in the (original) directory

    for dir_name, subdir_list, file_list in os.walk('.'):
        for filename in file_list:
            if not os.path.isdir(filename):
                convert_to_subdir_v2(filename, dir_names)

    #
    # for filename in os.listdir('.'):
        # ignore directories, just process files


    # NOTE: These options won't just work...
    # they show you ways of renaming and moving files,
    # but you need to have valid filenames. You can't make a file with
    # a blank name, and on Windows you can't have files with the same
    # characters but different case (e.g. a.TXT and A.txt)
    # So, you need to get valid filenames before you can use these.

    # Option 1: rename file to new name - in place
    # os.rename(filename, new_name)

    # Option 2: move file to new place, with new name
    # shutil.move(filename, 'temp/' + new_name)

    # Processing subdirectories using os.walk()

    # os.chdir('..')  # .. means "up" one directory



def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # First, replace the spaces and .TXT (the easy part)
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")

    new_name = ""

    prev_char = ''

    for char in filename:
        if char.isupper() and prev_char.islower():
            char = char.replace(char, "_" + char)
        prev_char = char
        new_name += char

    return new_name

# Version 1
current_extensions = []
def convert_to_subdir(filename):

    extension = filename[filename.find(".")+1:]
    if extension in current_extensions:
        shutil.move(filename, extension)
    else:
        os.mkdir(extension)
        shutil.move(filename, extension)
        current_extensions.append(extension)

def convert_to_subdir_v2(filename, dir_names):
    extension = filename[filename.find(".") + 1:]
    choice = input("what category would you like to sort {} files into? ".format(extension))
    if choice in dir_names.keys():
        dir_names[choice] = dir_names[choice] + " " + extension
    else:
        dir_names[choice] = extension
    print(dir_names)
    # shutil.move(filename,new_dir_name)


main()
