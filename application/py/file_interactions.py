"""Project Ideas for Code"""
import os
import shutil
import sys
import eyed3



#linux version
#identifies all files with '.mp3' type and adds them to list
def identify_mp3_lx(path):
    list_of_mp3s = list()
    for file in os.listdir(path):  # Goes through files checking for .mp3/.wav/.flac files
        if file.endswith(".mp3"):
            list_of_mp3s.append(file)
    return list_of_mp3s


#Adds \\ between path and desired folder 

#linux version
def double_backslash_lx(path,folder):
    path_and_folder = path + "/" + folder
    #print (path_and_folder)
    return path_and_folder


#given a path and a folder; function checks for existance in directory path
#linux version
def folder_identify_lx(path,check_folder):
    path_and_folder = double_backslash_lx(path,check_folder) #uses function to avoid python \ problems
    #print(os.path.isdir(path_and_folder))
    return (os.path.isdir(path_and_folder))
#similar to folder identify, instead identifies if theres a file
def file_identify_lx(path,check_folder):
    path_and_folder = double_backslash_lx(path,check_folder) #uses function to avoid python \ problems
    #print(os.path.isdir(path_and_folder))
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
#linux version of Folder check
def folder_check_lx(directory_path):
    sub_genres = ["liquid","hiphop"]#,"neurofunk","trance","hardstyle","dubstep","rock"]
    masterdir_created = ""
    masterdir_exists = ""
    dir_created = ""
    dir_exists = ""
    
    try: # attempt to make a directory in desired locaiton
        os.mkdir(directory_path)
    except FileExistsError: # if directory already exists it catchs exception and informs user 
        masterdir_exists += "MASTER Directory: music "
    else:
        masterdir_created += "MASTER Directory: music"
    
    for item in sub_genres:
        path_and_folder = double_backslash_lx(directory_path,item)
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
#for windows testing purposes to save time manually writing \\ instead of \
def dircheck():
    dircheck = input("insert directory")
    print (doubleslash_checker(dircheck))

def move_files(path1,path2):
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
#linux version of move files
def move_files_lx(path1,path2):
    try:
        os.rename(path1, path2)
    except FileNotFoundError:
        return False
    else: 
        return True
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
            track_id3_tags.append(title) 
            track_id3_tags.append(album)
            track_id3_tags.append(artist)
            track_id3_tags.append(genre)
            return track_id3_tags
    else:
        return False
 #eye3d has error text in output that needs to be removed if output is to be used
 #Turns out I misunderstood the error
def strip_eyed3(eyed3_output):
    return eyed3_output.split("\n",1)[1]
