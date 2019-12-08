"""project imports"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
from application.models import Tracks, Artists, Genres
from application.py.file_interactions import identify_mp3, double_backslash_lx,folder_identify_lx, folder_check, move_files
from application.__init__ import LoginManager
from flask_login import LoginManager, current_user

"""  Project forms   """
class DirectoryForm(FlaskForm): #user enters directory path
    directory_path = StringField("Enter your directory: ",
    validators = [
        DataRequired(),
        Length(min=2, max = 150) 
    ]
    )
    submit = SubmitField ('Submit')

    def validate_directory_path(self,directory_path):
        in_use = folder_identify_lx(directory_path,"")
        if in_use:
            raise ValidationError("Directory already exists")
        if in_use == False:
            folder_check_lx(directory_path,"")
            #change me <-- add make a directory function

class GenreForm(FlaskForm): #allows user to enter genre name
    genre_name = StringField("Genre name: ",
    validators = [
        DataRequired(),
        Length(min=2, max = 20)
            ]
        )
    folder_path = StringField("Folder Path: ", default="/harvey/music")
    submit = SubmitField('Add Genre') #button to submit data
    
    def validate_genre_name(self,genre_name):
        in_use = Genres.query.filter_by(name=genre_name.data).first()
        if in_use:
            raise ValidationError("Genre Already exists")
    #def validate_folder_path(self,folder_path):
     #   in_use = folder_identify_lx("harvey/music" + (genre_name.data))
      #  if in_use:
       #     raise ValidationError("Directory already exists")

class SortForm(FlaskForm): #User chooses to sort music 
    submit = SubmitField ("Sort Library")

#allows user to enter an artist name and amend the default_genre of that artist
class UpdateArtistsForm(FlaskForm): #
    artist_name = StringField("Artist Name",
    validators = [
        DataRequired(),
        Length(min=2, max = 30)
    ])

    new_default_genre = StringField("Genre for artist",
    validators = [
        DataRequired(),
        Length(min = 3, max = 99)
    ])
    submit = SubmitField ("Change default genre")

    def validate_artist_name(self,artist_name):
        exists = Artists.query.filter_by(name = artist_name).first()
        if exists==False:
            raise ValidationError("Artist Does Not exist yet so you cant add a genre")
    
class DeleteASong(FlaskForm):
    song_title = StringField("Song Name:",
    validators = [
        DataRequired,
        Length(min = 2, max = 50)
    ]
    )
    submit = SubmitField ("Delete this song")

    def validate_title_name(self,song_name):
        exists = Tracks.query.filter_by(title = song_title).first
        if exists == False:
            raise ValidationError("Song doesn't exist")


