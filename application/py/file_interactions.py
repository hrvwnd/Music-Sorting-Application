"""Project Ideas for Code"""
import os
import shutil

def identify_mp3():
    #path = "C:\\Users\\Admin\\PycharmProjects\\pycharmtest"  # path of folder mp3 files download into
    path = "C:\\Users\\Admin\\Desktop\\try_to_use_git\\harvey._assessment\\music"
    #path = "C:\\Users\\harve\\Documents\\NEW_qa_coding\\project_music_sort-\\music"
    # remember formatting with "C:\\Users\\Admin\\blahblah\\blah" with double \ (\\)
    for file in os.listdir(path):  # Goes through files checking for .mp3/.wav/.flac files
        if file.endswith(".mp3") or file.endswith(".flac") or file.endswith(".wav"):
            if file.endswith(".flac"):  # flac is often unplayable on rekordbox software
                print("This file: ", file, "will most likely not be playable on DJ hardware, Continue? ")
                ask_user_again = True
                while ask_user_again:
                    user_continue = input()
                    if user_continue in ["y", "Y", "Yes", "yes"]:
                        ask_user_again = False
                        print("file: ", file)
                        CHANGEMETODOSOMETHING = "Change this"
                        # return file to sorting function - read id3 tags
                        # return file
                    elif user_continue in ["n", "N", "no", "No"]:
                        ask_user_again = False
                        print("file: ", file)
                        blahblah = "changethis"
                        # To do: Delete file and add deleted file name to list of files to replace
            else:
                print("file: ", file)
                thisshouldalsodosomething = "change this"
                
#Adds \\ between path and desired folder 
#windows version (file path \)
def double_backslash(path,folder):
    path_and_folder = path + "\\" + folder
    print (path_and_folder)
    return path_and_folder
#linux version
def double_backslash_lx(path,folder):
    path_and_folder = path + "/" + folder
    print (path_and_folder)
    return path_and_folder
    
#given a path and a folder; function checks for existance in directory path
def folder_identify(path,check_folder): 
    path = "C:\\Users\\Admin\\PycharmProjects\\pycharmtest"  # path of folder mp3 files download into
    path = "C:\\Users\\Admin\\Desktop\\try_to_use_git\\harvey._assessment\\music"
    #check_folder = "liquid"
    path_and_folder = double_backslash(path,check_folder) #uses function to avoid python \ problems
    print(os.path.isdir(path_and_folder))
    return (os.path.isdir(path_and_folder))
folder_identify("C:\\Users\\Admin\\Desktop\\try_to_use_git\\harvey\\music","liquid")




#folder_identify()  # testing function




def folder_check():
    sub_genres = ["liquid","hiphop"]#,"neurofunk","trance","hardstyle","dubstep","rock"]
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
def move_files():
    path1 = "C:\\Users\\harve\\Documents\\qacoding\\harvey._assessment\\music\\liquid.mp3"
    path2 = "C:\\Users\\harve\\Documents\\qacoding\\harvey._assessment\\music\\liquid\\liquid.mp3"
    try:
        os.rename(path1, path2)
    except FileNotFoundError:
        print ("Error: Check file directories are correct: \n", path1, "\n", path2)
    try:
        shutil.move(path1,path2)
    except FileNotFoundError:
        print ("Error: Check file directories are correct: \n", path1, "\n", path2)
