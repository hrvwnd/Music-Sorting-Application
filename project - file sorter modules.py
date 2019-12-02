"""Project Ideas for Code"""


def identify_mp3():
    import os
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


def folder_identify():
    import os  # needed to navigate directories
    path = "C:\\Users\\Admin\\PycharmProjects\\pycharmtest"  # path of folder mp3 files download into
    path = "C:\\Users\\Admin\\Desktop\\try_to_use_git\\harvey._assessment\\music"
    check_folder = "liquid"
    path_and_folder = double_backslash(path,check_folder)
    print(os.path.isdir(path_and_folder))


def double_backslash(path,folder):
    path_and_folder = path + "\\\\" + folder
    print (path_and_folder)
    return path_and_folder


#double_backslash("C:\\Users\\Admin\\PycharmProjects\\pycharmtest","rock") #  testing function
folder_identify()  # testing function

# identify_mp3() #  testing function
from abc import ABC, abstractmethod
class Music(ABC):
    def __init__(self,title,artist,genre):
        self.title = title
        self.artist = artist
        self.genre = genre
        def duration(self):
            pass
        def key(self):
            pass
        def comments(self):
            pass



"""I have no idea what this does change me"""
#class id3tags(file_info):
#    tags = { "title": ( 3, 33, stripnulls),
#             "artist": (33, 63, stripnulls),
#             "albums": (63, 93, stripnulls),
#             "year": (93, 97, stripnulls),
#             "comment": (97, 126, stripnulls),
#            "genre": (127,128,ord)}


