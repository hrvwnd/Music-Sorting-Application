"""Project Ideas for Code"""
import os
import shutil
import sys
import eyed3

#windows app version of code
def identify_mp3(path):
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

#linux version
#identifies all files with '.mp3' type and adds them to list
def identify_mp3_lx(path):
    list_of_mp3s = list()
    for file in os.listdir(path):  # Goes through files checking for .mp3/.wav/.flac files
        if file.endswith(".mp3"):
            list_of_mp3s.append(file)
    return list_of_mp3s


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
#windows version
def folder_identify(path,check_folder): 
    #check_folder = "liquid"
    path_and_folder = double_backslash(path,check_folder) #uses function to avoid python \ problems
    print(os.path.isdir(path_and_folder))
    return (os.path.isdir(path_and_folder))


#linux version
def folder_identify_lx(path,check_folder):
    path_and_folder = double_backslash_lx(path,check_folder) #uses function to avoid python \ problems
    print(os.path.isdir(path_and_folder))
    return (os.path.isdir(path_and_folder))

def file_identify_lx(path,check_folder):
    path_and_folder = double_backslash_lx(path,check_folder) #uses function to avoid python \ problems
    print(os.path.isdir(path_and_folder))
    return (os.path.isfile(path_and_folder))


#creates a single directory in a given path - used by routes.py: amend_directory
def create_single_folder(path,folder):
    path_and_folder = double_backslash_lx(path,folder)
    try: # attempt to make a directory in desired locaiton
        os.mkdir(path_and_folder)
    except FileExistsError: # if directory already exists it catchs exception and informs user 
        return False
    else:
        return True


#Search inside directory for specified folder
#if found; checks for subgenre folders
#if any folder is not found, it is created 
def folder_check(directory_path):
    sub_genres = ["liquid","hiphop"]#,"neurofunk","trance","hardstyle","dubstep","rock"]
    masterdir_created = ""
    masterdir_exists = ""
    dir_created = ""
    dir_exists = ""
    
    try: # attempt to make a directory in desired locaiton
        os.mkdir(directory_name)
    except FileExistsError: # if directory already exists it catchs exception and informs user 
        masterdir_exists += "MASTER Directory: music "
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


#linux version of Folder check
def folder_check_lx(directory_path):
    sub_genres = ["liquid","hiphop"]#,"neurofunk","trance","hardstyle","dubstep","rock"]
    masterdir_created = ""
    masterdir_exists = ""
    dir_created = ""
    dir_exists = ""
    
    try: # attempt to make a directory in desired locaiton
        os.mkdir(directory_name)
    except FileExistsError: # if directory already exists it catchs exception and informs user 
        masterdir_exists += "MASTER Directory: music "
    else:
        masterdir_created += "MASTER Directory: music"
    
    for item in sub_genres:
        path_and_folder = double_backslash_lx(directory_name,item)
        try:            
            os.mkdir(path_and_folder)
            dir_created += item + "\n"
        except FileExistsError:
            #print ("File exists")
            dir_exists += item + "\n"
    if masterdir_created != "":
        return masterdir_created, dir_created
    else:
        if dir_created != "":
            return masterdir_exists, dir_created
        else:
            return masterdir_exists, dir_exists


# To avoid python \ problems this function searchs for \\ and returns \\\\
# this is refered to python as just \\ 
def doubleslash_checker(file_path):
    return file_path.replace("\\","\\\\")    
def dircheck():
    dircheck = input("insert directory")
    print (doubleslash_checker(dircheck))

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

#uses function eyed3 to read id3 tags 
def mp3_id3_read(path,file_to_check):
    track_id3_tags = list()
    if file_identify_lx(path,file_to_check):
        try:
            path_and_file = double_backslash_lx(path,file_to_check)
            load_file = eyed3.load(path_and_file)
            title = load_file.tag.title
            album = load_file.tag.album
            artist = load_file.tag.artist
            genre = load_file.tag.genre
        except AttributeError:
            return "AttributeError"
        else:
            tack_id3_tags.append(title,album,artist,genre) 
            return track_id3_tags


