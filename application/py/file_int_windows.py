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

#windows version (file path \)
def double_backslash(path,folder):
    path_and_folder = path + "\\" + folder
    print (path_and_folder)
    return path_and_folder

#windows version
def folder_identify(path,check_folder): 
    #check_folder = "liquid"
    path_and_folder = double_backslash(path,check_folder) #uses function to avoid python \ problems
    print(os.path.isdir(path_and_folder))
    return (os.path.isdir(path_and_folder))

def folder_check(directory_path):
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
        path_and_folder = double_backslash(directory_path,item)
        try:            
            os.mkdir(path_and_folder)
            dir_created += item + "\n"
        except FileExistsError:
            #print ("File exists")
            dir_exists += item + "\n"

    if masterdir_created != "":
        print (masterdir_created + " has been created in " + directory_path)
    if dir_created != "":
        print(str(dir_created) + "\n genre folders have been created in: " + directory_path)
    if masterdir_exists != "":
        print (masterdir_exists + "already exists in " + directory_path)
    if dir_exists != "":
        print ("Pre-existing Genre folders: ")
        print (dir_exists) 

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
