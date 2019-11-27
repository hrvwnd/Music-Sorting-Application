"""A program to move files around folders within a directory"""

import shutil
import os

def move_files():
    path1 = 'C:\\Users\\harve\\Documents\\NEW_qa_coding\\project_music_sort-\\music\\liquid.mp3'
    path2 = 'C:\\Users\\harve\\Documents\\NEW_qa_coding\\project_music_sort-\\music\\liquid\\liquid.mp3'
    #src = "/C:/Users/harve/Documents/NEW_qa_coding/project_music_sort-/music/liquid.mp3"
    #dst = "/C:/Users/harve/Documents/NEW_qa_coding/project_music_sort-/music/liquid/liquid.mp3"
    #path1 = "\\music\\liquid.mp3"
    #path2 = "\\music\\liquid\\liquid.mp3"
    path1 = 'C:\\Users\\Admin\\Desktop\\try_to_use git\\project_music_sort\\music\\liquid.mp3'
    path2 = 'C:\\Users\\Admin\\Desktop\\try_to_use git\\project_music_sort\\music\\liquid'
    os.rename(path1, path2)
    #shutil.move(path1,path2)
move_files()


