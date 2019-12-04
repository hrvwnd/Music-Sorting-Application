"""Function to check for existing folders within directory"""
"""If folder does not exist it makes a new folder"""
import os 
from identify_mp3 import double_backslash


def folder_check():
    sub_genres = ["liquid","hiphop"]#,"neurofunk","trance"",hardstyle","hardcore","frenchcore","dubstep","rock"]
    #user_directory = input ("Enter your desired folder directory: ")
    #directory_name= "C:\\Users\\harve\\Documents\\NEW_qa_coding\\project_music_sort-\\music\\liquid"
    #directory_name = "\\Users\\Admin\\Desktop\\try to use git\\project_music_sort\\music"
    directory_name = "C:\\Users\\harve\\Documents\\NEW_qa_coding\\harvey\\music"
    directory_name = "C:\\Users\\Admin\\Desktop\\try_to_use_git\\harvey\\music"
    masterdir_created = ""
    masterdir_exists = ""
    dir_created = ""
    dir_exists = ""
    try: # attempt to make a directory in desired locaiton
        os.mkdir(directory_name)
        #print("Master Directory "+ directory_name+ " created")

    except FileExistsError: # if directory already exists it catchs exception and informs user 
        masterdir_exists += "MASTER Directory: music "
        #print("Master Directory "+ directory_name+ " already exists")
    else:
        masterdir_created += "MASTER Directory: music"
    
    for item in sub_genres:
        path_and_folder = double_backslash(directory_name,item)
        try:            
            os.mkdir(path_and_folder)
            dir_created += item + "\n"
        except FileExistsError:
            #print ("File exists")
            dir_exists += item + "\n"

    if masterdir_created != "":
        print (masterdir_created + " has been created in " + directory_name)
    if dir_created != "":
        print(str(dir_created) + "\n genre folders have been created in: " + directory_name)
    if masterdir_exists != "":
        print (masterdir_exists + "already exists in " + directory_name)
    if dir_exists != "":
        print ("Pre-existing Genre folders: ")
        print (dir_exists) 


# To avoid python \ problems this function searchs for \\ and returns \\\\
# this is refered to python as just \\ 
def doubleslash_checker(file_path):
    return file_path.replace("\\","\\\\")    
def dircheck():
    dircheck = input("insert directory")
    print (doubleslash_checker(dircheck))

#dircheck()
folder_check()