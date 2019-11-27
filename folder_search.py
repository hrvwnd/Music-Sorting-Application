"""Function to check for existing folders within directory"""
"""If folder does not exist it makes a new folder"""

def folder_check():
    import os 
    directory_name= "C:\\Users\\harve\\Documents\\NEW_qa_coding\\project_music_sort-\\music\\liquid"
    directory_name = "\\Users\\Admin\\Desktop\\try to use git\\project_music_sort\\music"
    try:
        os.mkdir(directory_name)
        print("Directory ", directory_name, " created")
        return True
    except FileExistsError:
        print("Directory ", directory_name, " already exists")
        return False 
