"""Function to check for existing folders within directory"""
"""If folder does not exist it makes a new folder"""
import os 
from identify_mp3 import double_backslash


def folder_check():
    sub_genres = ["liquid","hiphop","neurofunk","trance"",hardstyle","hardcore","frenchcore","dubstep","rock"]
    #user_directory = input ("Enter your desired folder directory: ")
    #directory_name= "C:\\Users\\harve\\Documents\\NEW_qa_coding\\project_music_sort-\\music\\liquid"
    #directory_name = "\\Users\\Admin\\Desktop\\try to use git\\project_music_sort\\music"
    directory_name = "C:\\Users\\harve\\Documents\\NEW_qa_coding\\harvey\\music"
    try:
        os.mkdir(directory_name)
        print("Directory ", directory_name, " created")
        #return True
    except FileExistsError:
        print("Directory ", directory_name, " already exists")
        #return False 
    for item in sub_genres:
        path_and_folder = double_backslash(directory_name,item)
        dir_created = []
        dir_exists = []
        try:            
            os.mkdir(path_and_folder)
            dir_created.append(item)
        except FileExistsError:
            dir_exists.append(item)
    if dir_created != []:
        print(str(dir_created) + "\n genre folders have been created in: \n" + directory_name)
    elif dir_exists != []:
        print (str(dir_exists)+ "\n genre folders already exist in " + directory_name)
    print (dir_exists) 

def doubleslash_checker(file_path):
    return file_path.replace("\\","\\\\")    

folder_check()
